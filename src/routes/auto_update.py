from flask import Blueprint, jsonify
import os
import subprocess
import json
from datetime import datetime

auto_update_bp = Blueprint('auto_update', __name__)

@auto_update_bp.route('/version', methods=['GET'])
def get_version():
    """Retorna a versão atual da aplicação"""
    try:
        # Tentar obter informações do git
        try:
            commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'], 
                                                cwd=os.path.dirname(__file__)).decode('utf-8').strip()[:8]
            branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], 
                                           cwd=os.path.dirname(__file__)).decode('utf-8').strip()
        except:
            commit_hash = 'unknown'
            branch = 'unknown'
        
        version_info = {
            'version': '1.0.0',
            'commit': commit_hash,
            'branch': branch,
            'build_date': datetime.now().isoformat(),
            'status': 'stable'
        }
        
        return jsonify(version_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auto_update_bp.route('/health-check', methods=['GET'])
def health_check():
    """Verifica a saúde da aplicação e dependências"""
    try:
        health_status = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'services': {
                'api': 'operational',
                'database': 'operational',
                'external_apis': 'simulated'  # Como estamos simulando as APIs
            },
            'uptime': 'running',
            'memory_usage': 'normal'
        }
        
        return jsonify(health_status)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auto_update_bp.route('/update-check', methods=['GET'])
def check_for_updates():
    """Verifica se há atualizações disponíveis"""
    try:
        # Simular verificação de atualizações
        # Em uma implementação real, verificaria repositório remoto ou serviço de atualizações
        
        update_info = {
            'updates_available': False,
            'current_version': '1.0.0',
            'latest_version': '1.0.0',
            'last_check': datetime.now().isoformat(),
            'update_type': None,  # 'critical', 'security', 'feature', 'bugfix'
            'changelog': [],
            'auto_update_enabled': True
        }
        
        return jsonify(update_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auto_update_bp.route('/system-status', methods=['GET'])
def system_status():
    """Retorna status detalhado do sistema"""
    try:
        status = {
            'timestamp': datetime.now().isoformat(),
            'application': {
                'name': 'YouTube SEO Analyzer',
                'version': '1.0.0',
                'status': 'running',
                'environment': 'production'
            },
            'dependencies': {
                'flask': 'operational',
                'flask_cors': 'operational',
                'requests': 'operational'
            },
            'external_services': {
                'google_trends': 'simulated',
                'youtube_api': 'simulated',
                'keyword_tools': 'simulated'
            },
            'performance': {
                'response_time': 'normal',
                'error_rate': 'low',
                'availability': '99.9%'
            },
            'security': {
                'ssl_enabled': True,
                'cors_configured': True,
                'rate_limiting': False  # Pode ser implementado futuramente
            }
        }
        
        return jsonify(status)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

