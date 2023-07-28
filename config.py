"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "27957041")
        self.API_HASH: str = os.environ.get("API_HASH", "2ae1c9912cd2efdecae7f0208994f0b0")
        self.SESSION: str = os.environ.get("SESSION", "BQCO5p9kWJ8G5ju4XLWE_eMQQEEBXYcNKaOiJBVR6zL1KjAI1qZM7Pj01_qjldNCJWMvSRStqibhVC_wcTGviELKpfsYCvp8BE4rMOKF8l40ACvLzXSCLko_fkvJsr2_mr0mD_2M0uweFeEhNZGAxHooIOgb-cYmRxwDtoB34M92xDZGOS8mZJSXoKZolhhbVWgXXcQeUlliLYgg8B7GLYueO0-ynT32P_pY47I3V3fIH-6oTzHqQr9PGZ3XQRA1Q7mpHh4-ZPxLAofCFU6mB8CH-dYrYRX7obMfdjiklFEJUiJKmPwPfbUPYbe3CwqkS4TNvZqsWjp5OY1f9NMWiWyQAAAAATmDeAIA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "6041305578:AAHifZOeb5UURh-X8APKhBVWCidv8aZvI_A")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5276467211").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = True
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
