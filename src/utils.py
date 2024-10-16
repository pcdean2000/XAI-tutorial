import matplotlib.pyplot as plt

def save_fig(fig_name, tight_layout=True, fig_extension="png", resolution=300):
    path = f"{fig_name}.{fig_extension}"
    print(f"Saving figure {fig_name}")
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)