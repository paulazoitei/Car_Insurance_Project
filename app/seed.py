
from __future__ import annotations
import random
from decimal import Decimal
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session


from app.db.session import engine, SessionLocal


from app.db.models.owner import Owner
from app.db.models.car import Car
from app.db.models.insurance_policy import InsurancePolicy
from app.db.models.claim import Claim
from app.db.models.policy_expiry_log import PolicyExpiryLog




random.seed(42)

VIN_CHARS = "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"
MAKES_MODELS = [
    ("Toyota", "Corolla"),
    ("VW", "Golf"),
    ("Ford", "Focus"),
    ("Skoda", "Octavia"),
    ("Renault", "Megane"),
    ("Hyundai", "i30"),
    ("Kia", "Ceed"),
    ("Honda", "Civic"),
    ("Mazda", "3"),
    ("BMW", "118d"),
]
FIRST_NAMES = ["Alex", "Mara", "Chris", "Iulia", "Vlad", "Andrei", "Roxana", "Teo", "Bianca", "Paul"]
LAST_NAMES = ["Ionescu", "Popescu", "Marin", "Dumitrescu", "Stan", "Radu", "Gheorghe", "Tudor", "Voicu", "Apostol"]

UTC = timezone.utc
NOW = datetime.now(UTC).replace(microsecond=0)

def make_vin() -> str:
    return "".join(random.choice(VIN_CHARS) for _ in range(17))

def bounded_year() -> int:
    return random.randint(2005, 2022)

def money(low=200, high=5000) -> Decimal:
    return Decimal(random.randint(low, high)) + Decimal("0.00")

def policy_window(kind_idx: int) -> tuple[datetime, datetime]:
    """
    Distribute 10 policies as: ~1/3 expired, ~1/3 active, ~1/3 future.
    """
    if kind_idx % 3 == 0:

        end = NOW - timedelta(days=random.randint(30, 300))
        start = end - timedelta(days=365)
    elif kind_idx % 3 == 1:

        start = NOW - timedelta(days=random.randint(10, 200))
        end = start + timedelta(days=365)
    else:

        start = NOW + timedelta(days=random.randint(10, 200))
        end = start + timedelta(days=365)
    return start, end

def claim_date_near(start: datetime, end: datetime) -> datetime:
    """
    Place claim dates around the policy window (some inside, some just outside)
    to give you edge cases for filtering.
    """
    span_days = max(10, (end - start).days)
    offset = random.randint(-15, span_days + 15)
    dt = start + timedelta(days=offset)
    return dt.replace(tzinfo=UTC, hour=random.randint(0, 23), minute=random.randint(0, 59), second=0, microsecond=0)

def main():
    session: Session = SessionLocal()
    try:
        # delete for run again without duplicates
        # session.query(PolicyExpiryLog).delete()
        # session.query(Claim).delete()
        # session.query(InsurancePolicy).delete()
        # session.query(Car).delete()
        # session.query(Owner).delete()
        # session.commit()

        owners: list[Owner] = []
        cars: list[Car] = []
        policies: list[InsurancePolicy] = []
        claims: list[Claim] = []
        logs: list[PolicyExpiryLog] = []


        for i in range(10):
            first = FIRST_NAMES[i % len(FIRST_NAMES)]
            last = LAST_NAMES[(i * 3) % len(LAST_NAMES)]
            owners.append(
                Owner(
                    name=f"{first} {last}",
                    email=f"{first.lower()}.{last.lower()}{i}@example.com",
                )
            )
        session.add_all(owners)
        session.flush()


        used_vins = set()
        for i in range(10):
            make, model = MAKES_MODELS[i % len(MAKES_MODELS)]
            vin = make_vin()
            while vin in used_vins:
                vin = make_vin()
            used_vins.add(vin)

            cars.append(
                Car(
                    vin=vin,
                    make=make,
                    model=model,
                    year_of_manufacture=bounded_year(),
                    owner_id=owners[i % len(owners)].id,
                )
            )
        session.add_all(cars)
        session.flush()


        providers = ["Allianz", "Groupama", "Generali", "Omniasig", "Uniqa", "ASITO"]
        for i, car in enumerate(cars):
            start, end = policy_window(i)
            policies.append(
                InsurancePolicy(
                    car_id=car.id,
                    provider=random.choice(providers),
                    start_date=start,
                    end_date=end,
                )
            )
        session.add_all(policies)
        session.flush()


        for i, (car, pol) in enumerate(zip(cars, policies)):
            cdate = claim_date_near(pol.start_date, pol.end_date)
            claims.append(
                Claim(
                    car_id=car.id,
                    claim_date=cdate,
                    description=f"Claim #{i+1}: {random.choice(['minor accident', 'glass damage', 'hail', 'scratch', 'parking bump'])}",
                    amount=money(200, 8000),
                )
            )
        session.add_all(claims)
        session.flush()


        for pol in policies:
            logs.append(
                PolicyExpiryLog(
                    policy_id=pol.id,
                    expired_at=pol.end_date,
                )
            )
        session.add_all(logs)

        session.commit()

        print("✅ Seed complete:")
        print(f" Owners: {len(owners)}")
        print(f" Cars:   {len(cars)}")
        print(f" Policies: {len(policies)}")
        print(f" Claims:   {len(claims)}")
        print(f" Expiry logs: {len(logs)}")

    finally:
        session.close()

if __name__ == "__main__":
    main()
