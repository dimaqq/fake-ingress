import scenario
from fake_ingress.charm import FakeIngressCharm

META = {
    "name": "fake-ingress",
    "provides": {
        "ingress": {
            "interface": "ingress"
        }
    }
}

def test_smoke():
    ctx = scenario.Context(FakeIngressCharm, meta=META)
    in_ = scenario.State(
        leader=True,
        relations=[scenario.Relation(endpoint="ingress", interface="ingress", remote_app_name="dummy")],
    )
    ctx.run(ctx.on.start(), in_)
