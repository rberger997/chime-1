#!/usr/bin/env python
"""Set defaults for your fork/locality here

   after we merge this in we can set defaults in a `config/env` type of file
"""

from collections import namedtuple

# (0.02, 7) is 2%, 7 days
# be sure to multiply by 100 when using as a default to the pct widgets!
RateLos = namedtuple('RateLos', ('rate', 'length_of_stay'))


class Regions:
    """Arbitrary number of counties."""
    def __init__(self, **kwargs):
        susceptible = 0
        for key, value in kwargs.items():
            setattr(self, key, value)
            susceptible += value
        self._susceptible = susceptible

    @property
    def susceptible(self):
        return self._susceptible


class Constants:
    def __init__(
        self, *,
        current_hospitalized: int,
        doubling_time: int,
        known_infected: int,
        n_days: int,
        relative_contact_rate: int,
        region: Regions,

        hospitalized: RateLos,
        icu: RateLos,
        ventilated: RateLos,
        market_share: float = 1.0
    ):
        self.region = region
        self.known_infected = known_infected
        self.current_hospitalized = current_hospitalized
        self.doubling_time = doubling_time
        self.market_share = market_share
        self.relative_contact_rate = relative_contact_rate

        self.hospitalized = hospitalized
        self.icu = icu
        self.ventilated = ventilated
        self.n_days = n_days

    def __repr__(self) -> str:
        return f"Constants(susceptible_default: {self.region.susceptible}, known_infected: {self.known_infected})"

