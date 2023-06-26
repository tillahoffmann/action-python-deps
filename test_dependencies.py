from matplotlib import pyplot as plt
import torch


def test_dependencies() -> None:
    x = torch.randn([100])
    y = x + 0.1 * torch.randn([100])

    _, ax = plt.subplots()
    ax.scatter(x, y)
