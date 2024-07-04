"""Fake Ingress."""
import logging

import ops
from charms.traefik_k8s.v2.ingress import IngressPerAppProvider
from ops.charm import RelationEvent


class FakeIngressCharm(ops.CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)
        self.per_app = IngressPerAppProvider(charm=self)
        self.framework.observe(self.per_app.on.data_provided, self.provided)
        self.farmework.observe(self.per_app.on.data_removed, self.removed)

    def provided(self, event: RelationEvent):
        logging.warning("proivided raw %s", event.snapshot())
        logging.warning("proivided %s",
                        [
                            event,
                            event.app,
                            event.unit,
                            event.relation,
                            event.relation.name,
                            event.relation.id,
                        ])
        self.per_app.publish_url(event.relation, "http://lb.example/")

    def removed(self, event: RelationEvent):
        logging.warning("removed raw %s", event.snapshot())

if __name__ == "__main__":  # pragma: nocover
    ops.main(FakeIngressCharm)  # type: ignore
