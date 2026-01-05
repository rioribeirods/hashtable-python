# 🏗️ Hash Table em Python

Uma implementação educacional completa de uma tabela hash (hash table) em Python, com tratamento de colisões, redimensionamento automático e interface similar a dicionários.

## 📋 Índice\
- [Visão Geral](#visão-geral)
- [Características](#características)
- [Como Usar](#como-usar)
- [API Completa](#api-completa)
- [Implementação Técnica](#implementação-técnica)
- [Testes](#testes)
- [Aprendizados](#aprendizados)
- [Comparação com `dict` Python](#comparação-com-dict-python)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## 🎯 Visão Geral

Esta é uma implementação educacional de uma **tabela hash** (também conhecida como mapa hash ou dicionário) que demonstra os princípios fundamentais de estruturas de dados. A implementação inclui tratamento de colisões, redimensionamento dinâmico e uma interface Python completa.

**Objetivos educacionais:**
- Entender como tabelas hash funcionam internamente
- Aprender sobre funções hash e tratamento de colisões
- Implementar métodos especiais do Python
- Praticar desenvolvimento orientado a testes (TDD)

## ✨ Características

- ✅ **Tratamento de colisões** com encadeamento separado (separate chaining)
- ✅ **Redimensionamento automático** quando o fator de carga excede 0.7
- ✅ **Interface completa** similar a dicionários Python
- ✅ **Métodos especiais** (`__getitem__`, `__setitem__`, `__len__`, etc.)
- ✅ **Iteração** sobre chaves, valores e pares
- ✅ **Cópia profunda** e comparação por igualdade
- ✅ **Construção a partir de dicionários** com `from_dict()`
- ✅ **Testes abrangentes** com pytest
- ✅ **Documentação completa** e código limpo

## 🚀 Como Usar

### Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/python-hashtable.git
cd python-hashtable

# Instale as dependências (apenas pytest)
pip install pytest pytest-unordered
```

### Exemplos Básicos
```python\
from hashtable import HashTable

# Criar uma tabela hash
ht = HashTable(capacity=10)

# Inserir elementos (igual a dicionários)
ht["nome"] = "João"
ht["idade"] = 25
ht["cidade"] = "São Paulo"

# Acessar elementos
print(ht["nome"])  # Saída: João

# Verificar existência
print("nome" in ht)  # Saída: True

# Iterar sobre elementos
for chave in ht:
    print(f"{chave}: {ht[chave]}")

# Converter para dicionário
dicionario = dict(ht.pairs)

# Criar a partir de dicionário
ht2 = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
```

## 📚 API Completa

### Métodos Principais

| Método | Descrição | Complexidade |\
|--------|-----------|--------------|\
| `ht[key] = value` | Insere ou atualiza um valor | O(1) médio |\
| `ht[key]` | Recupera um valor | O(1) médio |\
| `del ht[key]` | Remove um elemento | O(1) médio |\
| `key in ht` | Verifica existência | O(1) médio |\
| `len(ht)` | Retorna a capacidade | O(1) |\
| `ht.get(key, default)` | Recupera com valor padrão | O(1) médio |\
| `ht.clear()` | Remove todos os elementos | O(n) |\
| `ht.pop(key, default)` | Remove e retorna valor | O(1) médio |\
| `ht.popitem()` | Remove e retorna par arbitrário | O(1) médio |\
| `ht.update(other)` | Atualiza com outros pares | O(k) |\
| `ht.setdefault(key, default)` | Retorna ou insere padrão | O(1) médio |\
| `ht.copy()` | Cria cópia da tabela | O(n) |

### Propriedades

| Propriedade | Tipo | Descrição |\
|-------------|------|-----------|\
| `ht.capacity` | `int` | Capacidade total da tabela |\
| `ht.size` | `int` | Número de elementos armazenados |\
| `ht.load_factor` | `float` | Fator de carga (elementos/capacidade) |\
| `ht.keys` | `set` | Conjunto de todas as chaves |\
| `ht.values` | `list` | Lista de todos os valores |\
| `ht.pairs` | `set` | Conjunto de tuplas (chave, valor) |

### Métodos de Classe
- `HashTable.from_dict(dict, capacity=None)`: Cria HashTable a partir de dicionário

## 🔧 Implementação Técnica

### Estrutura de Dados
```python\
# Cada bucket é uma lista para tratamento de colisões
_buckets: List[List[Pair]] = [[] for _ in range(capacity)]

# Par chave-valor imutável
class Pair(NamedTuple):
    key: Any
    value: Any
```

### Função Hash
```python\
def _index(self, key):
    return hash(key) % self._capacity
```

### Tratamento de Colisões
- **Encadeamento Separado**: Cada bucket contém uma lista de pares
- Colisões são resolvidas adicionando elementos à lista do bucket

### Redimensionamento Automático
- **Fator de carga limite**: 0.7
- Quando excedido, a capacidade é dobrada
- Todos os elementos são rehashed para novos buckets

## 🧪 Testes

O projeto inclui testes abrangentes usando pytest:

```bash\
# Executar todos os testes
pytest

# Executar testes com detalhes
pytest -v

# Executar testes específicos
pytest test_hashtable.py::test_should_handle_collisions -v
```

### Cobertura de Testes
- ✅ Inserção, acesso e remoção
- ✅ Tratamento de colisões
- ✅ Redimensionamento automático
- ✅ Comparação e cópia
- ✅ Iteração
- ✅ Casos de borda e erros
- ✅ Compatibilidade com dicionários

## 🎓 Aprendizados

### Conceitos de Estruturas de Dados
1\. **Tabelas Hash**: Princípios fundamentais
2\. **Funções Hash**: Distribuição uniforme de chaves
3\. **Colisões**: Encadeamento vs. endereçamento aberto
4\. **Fator de Carga**: Balanceamento entre memória e performance
5\. **Redimensionamento**: Estratégias de rehashing

### Python Avançado
1\. **Métodos Especiais**: `__getitem__`, `__setitem__`, `__contains__`, etc.
2\. **Protocolos**: Iteração, representação string, comparação
3\. **Tipagem**: Anotações de tipo com `typing`
4\. **Properties**: Getters como atributos
5\. **Métodos de Classe**: Fábricas como `from_dict`

### Desenvolvimento de Software
1\. **TDD**: Desenvolvimento orientado a testes
2\. **Design de API**: Interface intuitiva e Pythonica
3\. **Código Limpo**: Legibilidade e manutenibilidade
4\. **Documentação**: Docstrings e exemplos

## 📊 Comparação com `dict` Python

| Característica | Esta HashTable | `dict` Python |
|----------------|----------------|---------------|
| Implementação | Python puro | C otimizado |
| Tratamento de Colisões | Encadeamento | Endereçamento aberto |
| Performance | Boa (educacional) | Excelente |
| Redimensionamento | Load factor 0.7 | Algoritmo complexo |
| Memória | Mais (listas) | Altamente otimizado |
| Casos de Uso | Aprendizado, customização | Produção |

Essa hash table foi criada inspirada no tutorial do site https://realpython.com/python-hash-table/ com algumas modificações de preferência pessoal.

Esse projeto é meramente educacional, foi desafiador e divertido para mim, e espero que seja para você também ;p