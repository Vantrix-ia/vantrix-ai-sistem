from worker.pipeline import run_pipeline


def start_worker():
    trend = "portable blender"
    run_pipeline(trend)


if __name__ == "__main__":
    start_worker()