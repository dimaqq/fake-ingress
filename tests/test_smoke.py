import scenario

from fake_ingress.charm import FakeIngressCharm


def test_smoke():
    ctx = scenario.Context(FakeIngressCharm, meta=dict(name="fake-ingress"))
