from datetime import datetime
from ..models.manifacturation import Manifacturation

def is_fabriqueur_available(user, start_dt: datetime, end_dt: datetime) -> bool:

    conflict = Manifacturation.objects.filter(
        user=user,
        start_date__lt=end_dt,
        end_date__gt=start_dt
    ).exists()
    return not conflict

