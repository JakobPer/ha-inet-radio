"""The iNetRadio integration."""

from __future__ import annotations

import logging

from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import INetRadioConfigEntry

PLATFORMS: list[Platform] = [Platform.NUMBER]

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: INetRadioConfigEntry) -> bool:
    """Set up iNetRadio from a config entry."""

    # entry.runtime_data = MyAPI(...)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: INetRadioConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
