import random
from api import getRandomApi


tres_letras = [
    "paz", "não", "fel", "céu", "ser", "vil", "sob", "mal", "ver", "mãe",
    "ter", "ego", "bem", "mas", "dom", "bom", "vir", "são", "vão", "dar",
    "ora", "que", "era", "elo", "luz", "nós", "com", "réu", "seu", "foi",
    "tal", "rol", "mim", "uma", "lua", "até", "hum", "por", "fim", "pós",
    "vis", "dor", "ato", "sol", "vez", "sem", "pai", "dia", "dou", "irá",
    "pro", "eis", "rua", "ler", "tez", "ode", "tão", "nem", "fiz", "voz",
    "ajo", "gay", "meu", "lei", "voo", "mau", "mão", "num", "afã", "pôr",
    "dês", "for", "rio", "olá", "daí", "cia", "lar", "sua", "jus", "fez",
    "ira", "via", "som", "sim", "nau", "amo", "rei", "tem", "boa", "más",
    "uso", "mês", "jaz", "ido", "asa", "uns", "lhe", "pal", "eco", "aia"
]

quatro_letras = [
    "amor", "fato", "mito", "viés", "você", "como", "caos", "esmo", "brio", "vide",
    "ação", "sede", "após", "pois", "vida", "casa", "auge", "saga", "medo", "ônus",
    "ermo", "suma", "vovó", "mote", "além", "sina", "tolo", "idem", "urge", "pela",
    "crer", "apto", "zelo", "veio", "pude", "tudo", "mais", "ruim", "amar", "área",
    "rude", "coxo", "para", "cota", "soar", "ater", "será", "fase", "ente", "auto",
    "doce", "trás", "voga", "logo", "onde", "deus", "pelo", "rima", "ante", "cedo",
    "jugo", "alma", "meio", "arte", "meta", "cujo", "sela", "numa", "traz", "sido",
    "cela", "teor", "noia", "face", "asco", "nojo", "isso", "alvo", "foco", "pose",
    "sair", "base", "vale", "ódio", "agir", "teve", "alto", "todo", "ócio", "rito",
    "eita", "irão", "novo", "ágil", "alva", "tese", "alta", "bojo", "nexo", "orla"
]

cinco_letras = [
    "sagaz", "âmago", "negro", "termo", "êxito", "mexer", "nobre", "senso", "afeto",
    "algoz", "ética", "plena", "mútua", "tênue", "fazer", "assim", "vigor", "sutil",
    "aquém", "porém", "seção", "fosse", "sanar", "poder", "audaz", "ideia", "cerne",
    "inato", "moral", "sobre", "desde", "muito", "justo", "honra", "quiçá", "torpe",
    "sonho", "razão", "etnia", "fútil", "ícone", "anexo", "amigo", "égide", "tange",
    "lapso", "haver", "expor", "dengo", "mútuo", "tempo", "casal", "então", "hábil",
    "seara", "boçal", "ávido", "ardil", "pesar", "saber", "causa", "graça", "dizer",
    "genro", "óbice", "posse", "coser", "dever", "pária", "brado", "tenaz", "prole",
    "sendo", "crivo", "comum", "corja", "temor", "detém", "ainda", "ânimo", "ápice",
    "estar", "ceder", "ânsia", "xibiu", "pauta", "digno", "assaz", "culto", "mundo",
    "atroz", "fugaz", "censo", "gleba", "forte", "vício", "vulgo", "cozer", "valha",
    "denso"
]

seis_letras = [
    "exceto", "cínico", "idôneo", "âmbito", "néscio", "índole", "mister", "vereda",
    "apogeu", "inócuo", "convém", "utopia", "sádico", "escopo", "ênfase", "idiota",
    "casual", "mérito", "alusão", "hostil", "anseio", "cético", "legado", "hétero",
    "pressa", "gentil", "alheio", "nocivo", "infame", "clichê", "defina", "paixão",
    "exímio", "afável", "adorno", "dádiva", "êxtase", "sóbrio", "larica", "adesão",
    "aferir", "astuto", "também", "otário", "sessão", "limiar", "solene", "glória",
    "julgar", "lábaro", "formal", "hábito", "apreço", "embora", "ensejo", "ímpeto",
    "eficaz", "outrem", "ocioso", "júbilo", "dispor", "difuso", "alento", "perene",
    "nuance", "facção", "escusa", "exílio", "cessão", "lúdico", "abster", "ilação",
    "alçada", "objeto", "acesso", "acento", "desejo", "axioma", "sanção", "tácito",
    "isento", "etéreo", "buscar", "mulher", "cortês", "cobiça", "mazela", "sisudo",
    "penhor", "eximir", "avidez", "receio", "vulgar", "remoto", "prazer", "quando",
    "fático", "sempre", "nômade", "asseio"
]

sete_letras = [
    "empatia", "aurélio", "cônjuge", "embuste", "exceção", "caráter", "efêmero",
    "prolixo", "verbete", "idílico", "análogo", "genuíno", "estória", "sublime",
    "família", "pêsames", "inferir", "apático", "sucinto", "acepção", "redimir",
    "astúcia", "pródigo", "cultura", "audácia", "estigma", "recesso", "virtude",
    "refutar", "icônico", "soberba", "cinismo", "estável", "exortar", "mórbido",
    "trivial", "mitigar", "síntese", "aspecto", "luxúria", "cordial", "sucesso",
    "alegria", "imputar", "escória", "anátema", "emergir", "ademais", "candura",
    "orgulho", "deboche", "excerto", "litígio", "almejar", "através", "contudo",
    "frívolo", "coragem", "saudade", "oriundo", "escroto", "alcunha", "ambíguo",
    "salutar", "austero", "amizade", "racismo", "quimera", "sensato", "ambição",
    "excesso", "relação", "erudito", "imersão", "fomento", "modesto", "parcial",
    "demanda", "colosso", "ciência", "exótico", "conciso", "piedade", "volátil",
    "notório", "bizarro", "isenção", "vigente", "padecer", "híbrido", "auferir",
    "intenso", "inércia", "emotivo", "ansioso", "sentido", "déspota", "profano",
    "límpido", "difusão"
]

oito_letras = [
    "inerente", "respeito", "peculiar", "denegrir", "genocida", "anuência", "deferido",
    "equidade", "prudente", "iminente", "essência", "pandemia", "misógino", "desgraça",
    "invasivo", "alienado", "eminente", "premissa", "abstrato", "extensão", "empírico",
    "conceito", "talarico", "ardiloso", "ascensão", "rapariga", "reiterar", "lascívia",
    "devaneio", "relativo", "prodígio", "passível", "conserto", "gratidão", "analogia",
    "inserção", "modéstia", "apologia", "ativista", "remissão", "inóspito", "destarte",
    "medíocre", "despeito", "fomentar", "monótono", "inefável", "respaldo", "retórica",
    "concerne", "alicerce", "sinônimo", "proceder", "metódico", "primazia", "perfídia",
    "história", "rechaçar", "portanto", "complexo", "demagogo", "consiste", "critério",
    "notívago", "espectro", "distinto", "sucumbir", "amálgama", "abnegado", "desfecho",
    "paradoxo", "suscitar", "singular", "escárnio", "contexto", "processo", "comunhão",
    "elegível", "objetivo", "vocábulo", "refletir", "impávido", "maestria", "obstante",
    "problema", "endêmico", "desígnio", "jurídico", "solícito", "instigar", "incrível",
    "redenção", "epifania", "mediante", "paralelo", "insípido", "imanente", "preceito",
    "resoluto", "genérico"
]

nove_letras = [
    "perspicaz", "recíproco", "concessão", "impressão", "escrúpulo", "supérfluo", "retificar",
    "paradigma", "dicotomia", "propósito", "presunção", "concepção", "hipócrita", "ratificar",
    "implícito", "plenitude", "essencial", "hegemonia", "corolário", "incidente", "esdrúxulo",
    "altruísmo", "vagabundo", "altruísta", "hermético", "aleatório", "esperança", "promíscuo",
    "persuadir", "confiança", "deliberar", "sapiência", "indelével", "demasiado", "diligente",
    "mesquinho", "impetuoso", "descrição", "regozijar", "resignado", "inusitado", "eminência",
    "compaixão", "prudência", "pretensão", "discrição", "analítico", "explícito", "ordinário",
    "percepção", "exequível", "subjetivo", "nostalgia", "autonomia", "autóctone", "companhia",
    "resolução", "fidedigno", "desdenhar", "dissensão", "expressão", "constante", "supressão",
    "taciturno", "imparcial", "autêntico", "paciência", "ignorante", "arrogante", "outrossim",
    "execrável", "desumilde", "discorrer", "restrição", "consoante", "obstinado", "jactância",
    "arcabouço", "cognitivo", "eloquente", "adjacente", "instância", "interesse", "limítrofe",
    "sintético", "iminência", "submissão", "presságio", "relevante", "irascível", "empecilho",
    "excelente", "liberdade", "ludibriar", "humildade", "aquisição", "plausível", "ambicioso",
    "convicção", "primícias"
]

dez_letras = [
    "dicionário", "intrínseco", "prescindir", "presunçoso", "diligência", "corroborar",
    "intempérie", "detrimento", "maturidade", "parcimônia", "referência", "inspiração",
    "inexorável", "pragmático", "prepotente", "incipiente", "disruptivo", "sororidade",
    "serenidade", "arbitrário", "indulgente", "auspicioso", "iniquidade", "pertinente",
    "sagacidade", "resignação", "hipocrisia", "preconizar", "precedente", "vislumbrar",
    "incidência", "lisonjeado", "suscetível", "entretanto", "disposição", "excêntrico",
    "subestimar", "preliminar", "tribulação", "fleumático", "depreender", "anacrônico",
    "equivocado", "escrutínio", "retrógrado", "indolência", "excelência", "ingerência",
    "democracia", "infortúnio", "compassivo", "contemplar", "importante", "pejorativo",
    "restringir", "sintetizar", "proposição", "primordial", "signatário", "conjuntura",
    "subjacente", "coercitivo", "intrínseca", "dissolução", "itinerário", "finalidade",
    "esplêndido", "alteridade", "pecuniária", "espontâneo", "designação",
    "transeunte", "necessário", "constância", "sarcástico", "pusilânime", "privilégio",
    "idoneidade", "desprovido", "verossímil", "pernóstico", "exacerbado", "felicidade",
    "relevância", "disciplina", "divergente", "inferência", "pernicioso", "disseminar",
    "satisfação", "reverberar", "meticuloso", "esporádico", "influência", "militância",
    "retumbante", "consolidar", "fornicação", "subversivo"
]

onze_letras = [
    "significado", "perspectiva", "resiliência", "dissimulado", "vicissitude", "complacente",
    "contundente", "peremptório", "comorbidade", "compreensão", "perspicácia", "expectativa",
    "pressuposto", "beneplácito", "subterfúgio", "preconceito", "experiência", "indiferente",
    "consonância", "pretensioso", "transcender", "imensurável", "contingente", "intensidade",
    "proeminente", "beligerante", "necessidade", "superficial", "concernente", "benignidade",
    "contencioso", "inenarrável", "animosidade", "intervenção", "incumbência", "vocabulário",
    "antagonismo", "cumprimento", "resistência", "indiferença", "reivindicar", "compreender",
    "supracitado", "subsequente", "estereótipo", "integridade", "diversidade", "ambiguidade",
    "deliberação", "especulação", "indulgência", "proveniente", "divergência", "elucubração",
    "indubitável", "austeridade", "prognóstico", "importância", "heterogêneo", "tergiversar",
    "benevolente", "displicente", "negligência", "identificar", "oportunista", "estabelecer",
    "conveniente", "redundância", "consciência", "congruência", "discriminar", "pragmatismo",
    "substantivo", "excepcional", "providência", "admoestação", "conferência", "facultativo",
    "sistemático", "compulsório", "comprimento", "verborragia", "intersecção", "subordinado",
    "intelectual", "melancólico", "contradição", "relativizar", "generalizar", "desenvolver",
    "substancial", "honestidade", "dificuldade", "retificação", "conservador", "procedência",
    "autoritário", "amabilidade", "determinado", "antagonista"
]

doze_letras = [
    "perseverança", "condolências", "remanescente", "prerrogativa", "extrovertido",
    "complacência", "procrastinar", "discrepância", "determinação", "independente",
    "consequência", "intermitente", "conveniência", "benevolência", "compartilhar",
    "eclesiástico", "contingência", "transgressão", "felicitações", "consideração",
    "não obstante", "concomitante", "convergência", "cordialidade", "conhecimento",
    "cumplicidade", "convencional", "subsistência", "disseminação", "proselitismo",
    "sistematizar", "coincidência", "complexidade", "prescindível", "controvérsia",
    "imprevisível", "impertinente", "inverossímil", "escatológico", "displicência",
    "interlocutor", "ninfomaníaco", "libertinagem", "conformidade", "proporcionar",
    "intempestivo", "maledicência", "extemporâneo", "fraternidade", "intolerância",
    "resplandecer", "perseverante", "misericórdia", "estabilidade", "mediocridade",
    "persistência", "coexistência", "maquiavélico", "circunspecto", "preeminência",
    "aquiescência", "hermenêutica", "protagonista", "complementar", "parcialmente",
    "proeminência", "introvertido", "consolidação", "oportunidade", "constituição",
    "destinatário", "escarnecedor", "deslumbrante", "estigmatizar", "consistência",
    "parcialidade", "entendimento", "interessante", "caracterizar", "incircunciso",
    "procedimento", "generosidade", "condicionado", "circuncidado", "enclausurado",
    "superestimar", "fragmentação", "literalmente", "desenvoltura", "proficiência",
    "prosperidade", "depreciativo", "legitimidade", "simplicidade", "profissional",
    "incolumidade", "ininterrupto", "sobremaneira", "inescrutável", "beneficência"
]

treze_letras = [
    "reciprocidade", "contemporâneo", "inconveniente", "heterossexual", "circunstância",
    "discernimento", "solidariedade", "promiscuidade", "ressignificar", "intransigente",
    "credibilidade", "discriminação", "transcendente", "aprovisionado", "epistemologia",
    "contrapartida", "assintomático", "comprobatório", "perpendicular", "incongruência",
    "reminiscência", "ressentimento", "estereotipado", "possibilidade", "recenseamento",
    "intermediário", "veementemente", "preponderante", "indispensável", "subjetividade",
    "hodiernamente", "singularidade", "subserviência", "longanimidade", "convalescença",
    "pormenorizado", "transformação", "autenticidade", "independência", "incontinência",
    "instabilidade", "superveniente", "sensibilidade", "introspectivo", "reivindicação",
    "elegibilidade", "superestimado", "contraditório", "indissociável", "multifacetado",
    "eventualmente", "latifundiário", "recalcitrante", "desmistificar", "incredulidade",
    "quintessência", "inconsequente", "a despeito de", "sobressalente", "filho pródigo",
    "ininteligível", "inescrupuloso", "comportamento", "personalidade", "indescritível",
    "integralmente", "implementação", "monossilábico", "homogeneidade", "magnificência",
    "provavelmente", "precipuamente", "peculiaridade", "circunscrição", "consentimento",
    "incondicional", "convalescente", "remanejamento", "serendipidade", "contentamento",
    "consciencioso", "correlacionar", "arrefecimento", "incandescente", "predisposição",
    "versatilidade", "conscientizar", "desnecessário", "irresponsável", "supersticioso",
    "indeterminado", "imperceptível", "representação", "especificação", "identificação",
    "reconciliação", "incognoscível", "ressarcimento", "receptividade", "monocromático"
]

quatorze_letras = [
    "imprescindível", "condescendente", "idiossincrasia", "característica", "concupiscência",
    "extraordinário", "demasiadamente", "intercorrência", "irrepreensível", "consubstanciar",
    "pronta-entrega", "incomensurável", "discricionário", "preponderância", "arbitrariedade",
    "especificidade", "posteriormente", "imprescritível", "intransponível", "contextualizar",
    "empreendimento", "ancestralidade", "entretenimento", "transcendental", "paulatinamente",
    "infraestrutura", "relacionamento", "arrependimento", "revolucionário", "imparcialidade",
    "superveniência", "bem-aventurado", "atenciosamente", "ponto de vista", "transcendência",
    "periodicamente", "reconhecimento", "democratização", "insignificante", "diligentemente",
    "inconsistência", "personificação", "despretensioso", "impessoalidade", "socioambiental",
    "espontaneidade", "funcionalidade", "trazer à baila", "cônjuge virago", "intransigência",
    "aplicabilidade", "desprendimento", "procrastinação", "principalmente", "potencialidade",
    "estelionatário", "procrastinador", "estratificação", "licenciosidade", "extraordinária",
    "prestatividade", "excentricidade", "inconveniência", "dissolutamente", "congratulações",
    "pusilanimidade", "exequibilidade", "epistemológico", "insubstituível", "individualismo",
    "biodiversidade", "resplandecente", "jurisprudência", "abundantemente", "coercitividade",
    "disponibilizar", "plausibilidade", "acessibilidade", "internalização", "credenciamento",
    "papibaquígrafo", "constantemente", "exclusivamente", "perfeccionista", "multiplicidade",
    "aleatoriamente", "menção honrosa", "impressionante", "questionamento", "implicitamente",
    "grandiloquente", "esclarecimento", "minuciosamente", "permissividade", "frequentemente",
    "indiscriminado", "intermunicipal", "concessionária", "sobrecarregado", "transfiguração"
]

todas_palavras = tres_letras + quatro_letras + cinco_letras + seis_letras + seis_letras + oito_letras + \
    nove_letras + dez_letras + onze_letras + \
    doze_letras + treze_letras + quatorze_letras


random = getRandomApi()
if random:
    palavra = random
else:
    palavra = random.choice(todas_palavras)
