"""Typefully API v2 client — handles all HTTP communication."""

import logging
from datetime import datetime

import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://api.typefully.com/v2"


class TypefullyClient:
    def __init__(self, api_key: str):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
        )

    # ------------------------------------------------------------------
    # Account helpers
    # ------------------------------------------------------------------

    def get_social_sets(self) -> list[dict]:
        """Return all social sets the API key can access."""
        resp = self.session.get(f"{BASE_URL}/social-sets")
        resp.raise_for_status()
        return resp.json()

    def get_me(self) -> dict:
        resp = self.session.get(f"{BASE_URL}/me")
        resp.raise_for_status()
        return resp.json()

    # ------------------------------------------------------------------
    # Draft creation
    # ------------------------------------------------------------------

    def create_draft(
        self,
        social_set_id: str,
        content: str,
        publish_at: datetime,
        platform: str = "threads",
    ) -> dict:
        """
        Schedule a single post on the given platform.

        publish_at must be a timezone-aware datetime; it is sent as ISO 8601 UTC.
        """
        publish_at_iso = publish_at.strftime("%Y-%m-%dT%H:%M:%S+00:00")

        payload = {
            "platforms": {
                platform: {
                    "enabled": True,
                    "posts": [{"text": content}],
                }
            },
            "publish_at": publish_at_iso,
        }

        logger.debug("POST /drafts payload: %s", payload)

        resp = self.session.post(
            f"{BASE_URL}/social-sets/{social_set_id}/drafts",
            json=payload,
        )

        if not resp.ok:
            logger.error(
                "Typefully API error %s: %s", resp.status_code, resp.text
            )
            resp.raise_for_status()

        return resp.json()

    # ------------------------------------------------------------------
    # Draft listing (used to avoid double-scheduling)
    # ------------------------------------------------------------------

    def list_drafts(
        self, social_set_id: str, limit: int = 50, offset: int = 0
    ) -> list[dict]:
        resp = self.session.get(
            f"{BASE_URL}/social-sets/{social_set_id}/drafts",
            params={"limit": limit, "offset": offset},
        )
        resp.raise_for_status()
        data = resp.json()
        # API returns {"results": [...], "count": N}
        return data.get("results", data) if isinstance(data, dict) else data
