from flask import Blueprint, request, jsonify
from app.services.post_service import PostService
from app.schemas.post_schema import post_input_schema, post_output_schema, posts_output_Schema
from marshmallow import ValidationError
post_bp = Blueprint('posts', __name__, url_prefix='/article')

post_service = PostService()

@post_bp.route('/<int:limit>/<int:offset>', methods=['GET'])
def getAllArticle(limit, offset):
    try:
        paginated_data = post_service.getAllArticle(limit, offset)
        return jsonify({
            'success': True,
            'data': paginated_data
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    
@post_bp.route('', methods=['POST'])
def createArticle():
    try:
        data = post_input_schema.load(request.form)
    except ValidationError as err:
        return jsonify(err.messages), 400

    try:
        posts = post_service.createArticle(data)
        return jsonify({
            'success': True,
            'data': post_output_schema.dump(posts)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@post_bp.route('/<int:id>', methods=['GET'])
def getArticleById(id):
    try:
        data = post_service.getArticleById(id)

        if not data:
            return jsonify({
                'success': False,
                'error': "Article Not Found!"
            }), 404
        return jsonify({
            'success': True,
            'data': post_output_schema.dump(data)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@post_bp.route('/<int:id>', methods=['PUT'])
def updateArticle(id):
    try:
        data = post_input_schema.load(request.form, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    try:
        posts = post_service.updateArticle(id, data)

        if posts is None:
            return jsonify({
                'success': False,
                'error': "Article Not Found!"
            }), 404
        
        return jsonify({
            'success': True,
            'data': post_output_schema.dump(posts)
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
        
@post_bp.route('/<int:id>', methods=['DELETE'])
def deleteArticle(id):
    try:
        data = post_service.deleteArticle(id)

        if not data:
            return jsonify({
                'success': False,
                'error': "Article Not Found!"
            }), 404
        return jsonify({
            'success': True,
            'data': 'Delete Article Success!'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500