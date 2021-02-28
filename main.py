from pypresence import Presence
from time import time

RPC = Presence("815323683693658123")
btns = [
    { 
       "label": "qiwi", 
       "url": "https://qiwi.com/n/HURTY"
    },
    { 
       "label": "DonationAlerts", 
       "url": "https://www.donationalerts.com/r/ytruh22"
    }
] 

RPC.connect()
RPC.update(
    state=None,
    details=None,
    start=time(),
    buttons=btns,
    large_image="bud" ,
    small_image=None,
    large_text=None,
    small_text=None
)
input()