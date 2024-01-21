from uvicorn import run

if __name__ == "__main__":
    run(
        'copilot_service.api:app',
        host="0.0.0.0",
        port=8080,
    )
