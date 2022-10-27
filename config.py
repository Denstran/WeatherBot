from dataclasses import dataclass


@dataclass
class Config:
    token: str = 'YOUR_TOKEN'
    payment_token: str = 'PAYMENT_TOKEN'
    admin_ids: int = 694767747
