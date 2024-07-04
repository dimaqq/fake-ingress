"""Fake Ingress."""
import logging

import ops

from charms.traefik_k8s.v2.ingress import IngressPerAppProvider


class FakeIngressCharm(ops.CharmBase):
    """Charm the service."""

    def __init__(self, framework: ops.Framework):
        super().__init__(framework)
        self.per_app = IngressPerAppProvider(charm=self)
        framework.observe(self.on["httpbin"].pebble_ready, self._on_httpbin_pebble_ready)
        framework.observe(self.on.config_changed, self._on_config_changed)

if __name__ == "__main__":  # pragma: nocover
    ops.main(FakeIngressCharm)  # type: ignore
