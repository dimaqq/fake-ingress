#!/usr/bin/env python3
""" Charm entrypoint. """
from ops import main

from fake_charm import FakeIngressCharm


if __name__ == "__main__":  # pragma: nocover
    main(FakeIngressCharm)  # type: ignore
