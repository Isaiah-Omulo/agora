# -*- coding: utf-8 -*-
__copyright__ = "Copyright (c) 2014-2017 Agora.io, Inc."


import flask

from src.RtcTokenBuilder2 import *


bp = flask.Blueprint('token_app', __name__)

@bp.route('/health', methods=('GET',))
def health():
    return {
        "status": "ok",
        "service": "agora-token-service"
    }, 200


@bp.route('/v1/token', methods=('GET',))
def token():
    app = flask.current_app
    req = flask.request
    app.logger.info('recv gen-token req from %s', req.remote_addr)

    query_info = req.args

    # Validate required params
    if 'channel_name' not in query_info or 'user_id' not in query_info:
        return {"error": "channel_name and user_id are required"}, 400

    channel_name = query_info['channel_name']
    user_id = query_info['user_id']  # Firebase UID (string)

    app_id = app.config['APP_ID']
    app_certificate = app.config['APP_CERTIFICATE']
    expiration_in_seconds = 12 * 60 * 60  # 12 hours

    try:
        token = RtcTokenBuilder.build_token_with_user_account(
            app_id,
            app_certificate,
            channel_name,
            user_id,
            Role_Publisher,
            expiration_in_seconds
        )
    except Exception as e:
        app.logger.exception("Token generation failed")
        return {"error": "token generation failed"}, 500

    return {
        "token": token,
        "channel_name": channel_name,
        "user_id": user_id,
        "expires_in": expiration_in_seconds
    }, 200


