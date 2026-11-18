"""GiftGenius AI – Flask application factory and entry point."""

from __future__ import annotations

from flask import Flask

from config import get_config
from routes import chat_bp, gift_bp, main_bp, report_bp, shopping_bp
from utils.logger import get_logger, setup_logging
from utils.ollama_client import OllamaClient


def create_app(config_name: str | None = None) -> Flask:
    """
    Create and configure the Flask application.

    Args:
        config_name: Optional Flask environment name.

    Returns:
        Configured Flask application instance.
    """
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    config_class = get_config(config_name)
    app.config.from_object(config_class)

    app.config["REPORTS_DIR"].mkdir(parents=True, exist_ok=True)
    (app.config["BASE_DIR"] / "instance").mkdir(parents=True, exist_ok=True)
    app.config["LOG_DIR"].mkdir(parents=True, exist_ok=True)

    setup_logging(app.config["LOG_DIR"], app.config["LOG_LEVEL"])
    logger = get_logger("app")

    app.extensions["ollama"] = OllamaClient(
        base_url=app.config["OLLAMA_BASE_URL"],
        model=app.config["OLLAMA_MODEL"],
        timeout=app.config["OLLAMA_TIMEOUT"],
    )

    app.register_blueprint(main_bp)
    app.register_blueprint(gift_bp)
    app.register_blueprint(shopping_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(report_bp)

    @app.errorhandler(404)
    def not_found(_error):  # type: ignore[no-untyped-def]
        from flask import render_template

        return render_template("404.html"), 404

    logger.info(
        "GiftGenius AI started | model=%s | ollama=%s",
        app.config["OLLAMA_MODEL"],
        app.config["OLLAMA_BASE_URL"],
    )
    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=app.config.get("DEBUG", False),
    )
