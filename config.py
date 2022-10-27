from dataclasses import dataclass


@dataclass
class Config:
    token: str = 'YOUR_BOT_TOKEN'
    payment_token: str = 'PAYMENT_TOKEN'
    admin_ids: int = 694767747
    open_weather_token = 'YOUR_OPEN_WEATHER_TOKEN'
