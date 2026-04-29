import time
from vantrix_proyet.worker.pipeline import run_pipeline

INTERVAL = 3600  # 1 hora


def start():
    print("🧠 VANTRIX SCHEDULER INICIADO")

    while True:
        print("\n⏱ Ejecutando pipeline...")
        run_pipeline()

        print(f"\n⏳ Esperando {INTERVAL} segundos...")
        time.sleep(INTERVAL)


if __name__ == "__main__":
    start()