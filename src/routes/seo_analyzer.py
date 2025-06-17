from flask import Blueprint, request, jsonify
import requests
import json
import time
from datetime import datetime, timedelta
import re

seo_bp = Blueprint('seo', __name__)

def get_google_trends_data(keyword):
    """
    Simula dados do Google Trends
    Em uma implementação real, usaria pytrends ou uma API de scraping
    """
    # Simulação de dados
    trends_data = {
        'interest_over_time': 75,  # Interesse de 0-100
        'trend_direction': 'rising' if hash(keyword) % 2 == 0 else 'falling',
        'related_queries': [
            f"{keyword} tutorial",
            f"{keyword} dicas",
            f"como fazer {keyword}",
            f"{keyword} passo a passo"
        ]
    }
    return trends_data

def get_youtube_search_data(keyword):
    """
    Simula dados de busca do YouTube
    Em uma implementação real, usaria YouTube Data API v3
    """
    # Simulação de dados de concorrência
    competition_score = hash(keyword) % 100
    
    if competition_score < 30:
        competition = 'baixa'
    elif competition_score < 70:
        competition = 'média'
    else:
        competition = 'alta'
    
    youtube_data = {
        'competition_level': competition,
        'estimated_results': (hash(keyword) % 50000) + 10000,
        'top_channels': [
            f"Canal {keyword.title()} Pro",
            f"{keyword.title()} Master",
            f"Dicas de {keyword.title()}"
        ]
    }
    return youtube_data

def get_keyword_volume_data(keyword):
    """
    Simula dados de volume de busca
    Em uma implementação real, integraria com APIs de keyword research
    """
    # Simulação baseada no hash da keyword para consistência
    base_volume = hash(keyword) % 100000
    volume = max(1000, base_volume)  # Mínimo de 1000 buscas
    
    volume_data = {
        'monthly_searches': volume,
        'difficulty_score': (hash(keyword) % 100) + 1,
        'cpc': round((hash(keyword) % 500) / 100, 2),
        'seasonal_trend': 'stable'
    }
    return volume_data

def generate_seo_content(keyword):
    """
    Gera conteúdo SEO baseado na palavra-chave
    """
    # Palavra gancho para thumbnail
    ganchos = ['INCRÍVEL', 'SEGREDO', 'REVELADO', 'EXCLUSIVO', 'NOVO', 'VIRAL', 'TOP']
    palavra_gancho = ganchos[hash(keyword) % len(ganchos)]
    
    # Formatar palavra-chave mestre
    palavra_chave_mestre = f"{keyword} [Tutorial Completo] [Passo a Passo]"
    
    # Gerar descrição
    descricao = f"Aprenda tudo sobre {keyword} neste tutorial completo! Descubra as melhores técnicas e estratégias para dominar {keyword}. Não perca essa oportunidade única de se tornar um expert em {keyword}!"
    
    # Gerar hashtags
    keyword_clean = re.sub(r'[^a-zA-Z0-9]', '', keyword.replace(' ', ''))
    hashtag_mestre = f"#{keyword_clean}"
    hashtags = f"#{keyword_clean} #Tutorial #Dicas #ComoFazer #Iniciantes #Completo"
    
    # Gerar tags
    tags_mestre = f"{keyword}, tutorial, guia completo, passo a passo"
    tags_completas = f"{keyword}, tutorial, guia, dicas, como fazer, iniciantes, completo, {keyword} tutorial, aprenda {keyword}"
    
    seo_content = {
        'palavra_gancho': palavra_gancho,
        'palavra_chave_mestre': palavra_chave_mestre,
        'descricao': descricao,
        'hashtag_mestre': hashtag_mestre,
        'hashtags': hashtags,
        'tags_mestre': tags_mestre,
        'tags_completas': tags_completas
    }
    
    return seo_content

@seo_bp.route('/analyze', methods=['POST'])
def analyze_keyword():
    try:
        data = request.get_json()
        
        if not data or 'tema' not in data:
            return jsonify({'error': 'Tema é obrigatório'}), 400
        
        tema = data['tema'].strip()
        
        if not tema:
            return jsonify({'error': 'Tema não pode estar vazio'}), 400
        
        # Simular delay de processamento
        time.sleep(1)
        
        # Obter dados das diferentes fontes
        trends_data = get_google_trends_data(tema)
        youtube_data = get_youtube_search_data(tema)
        volume_data = get_keyword_volume_data(tema)
        seo_content = generate_seo_content(tema)
        
        # Compilar resposta
        response = {
            'tema': tema,
            'volume_busca': f"{volume_data['monthly_searches']:,}",
            'tendencia': 'alta' if trends_data['trend_direction'] == 'rising' else 'baixa',
            'concorrencia': youtube_data['competition_level'],
            'seo': {
                'palavra_gancho': seo_content['palavra_gancho'],
                'palavra_chave_mestre': seo_content['palavra_chave_mestre'],
                'descricao': seo_content['descricao'],
                'hashtag_mestre': seo_content['hashtag_mestre'],
                'hashtags': seo_content['hashtags'],
                'tags_mestre': seo_content['tags_mestre'],
                'tags_completas': seo_content['tags_completas']
            },
            'dados_detalhados': {
                'trends': trends_data,
                'youtube': youtube_data,
                'volume': volume_data
            },
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': f'Erro interno do servidor: {str(e)}'}), 500

@seo_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

