{
  "openapi": "3.1.0",
  "info": {
    "title": "Whisper Speech-to-Text API",
    "description": "API para transcrição de áudio usando o modelo Whisper da OpenAI.",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": ""
    }
  ],
  "paths": {
    "/transcriptions": {
      "post": {
        "summary": "Envia áudio para transcrição",
        "description": "Recebe um arquivo de áudio e retorna o texto transcrito.",
        "operationId": "createTranscription",
        "requestBody": {
          "required": true,
          "content": {
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "required": ["file"],
                "properties": {
                  "file": {
                    "type": "string",
                    "format": "binary",
                    "description": "Arquivo de áudio para transcrever (ex: mp3, wav, m4a)."
                  },
                  "language": {
                    "type": "string",
                    "description": "Idioma esperado no áudio (opcional, ex: 'pt', 'en')."
                  },
                  "model": {
                    "type": "string",
                    "description": "Modelo Whisper a ser utilizado.",
                    "default": "whisper-1"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Transcrição concluída com sucesso",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": { "type": "string", "example": "tr_12345" },
                    "text": { "type": "string", "example": "Olá, este é um teste de transcrição." },
                    "language": { "type": "string", "example": "pt" }
                  }
                }
              }
            }
          },
          "400": { "description": "Requisição inválida (formato incorreto, arquivo ausente)" },
          "500": { "description": "Erro interno do servidor" }
        }
      }
    },
    "/transcriptions/{id}": {
      "get": {
        "summary": "Consulta status ou resultado da transcrição",
        "description": "Retorna o status ou o resultado final de uma transcrição enviada.",
        "operationId": "getTranscription",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": { "type": "string" },
            "description": "ID da transcrição"
          }
        ],
        "responses": {
          "200": {
            "description": "Detalhes da transcrição",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": { "type": "string" },
                    "status": { "type": "string", "enum": ["queued", "processing", "completed", "failed"] },
                    "text": { "type": "string", "nullable": true },
                    "error": { "type": "string", "nullable": true }
                  }
                }
              }
            }
          },
          "404": { "description": "Transcrição não encontrada" }
        }
      }
    },
    "/languages": {
      "get": {
        "summary": "Lista idiomas suportados",
        "description": "Retorna uma lista de idiomas disponíveis para transcrição.",
        "operationId": "listLanguages",
        "responses": {
          "200": {
            "description": "Lista de idiomas",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "languages": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "code": { "type": "string", "example": "pt" },
                          "name": { "type": "string", "example": "Português" }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
