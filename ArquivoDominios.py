from apps.fiscal import models
from apps.financeiro import models as modelsf
from apps.admcore import models as modelsadm
import re

EMPRESA_ID = 1

DATA_EMISSAO_INICIO = "2024-07-01"
DATA_EMISSAO_FIM = "2024-07-31"

REGISTRO0000 = {"REGISTRO":"00000",
                "CNPJ":modelsadm.Empresa.objects.get(id=EMPRESA_ID).cpfcnpj}

print "|{}|{}".format(REGISTRO0000["REGISTRO"], re.sub(r"[^\w\s]", "", REGISTRO0000["CNPJ"]))


def ValidadorDados(VER, dado):
	#validar existência
    if VER == 1:
        if dado != None:
            return dado
        else:
            return ""
    #validar tamanho de nome, máximo 150 caracteres
    elif VER == 2:
        return dado.cliente.pessoa.nome[:150]
    #validar tamanho de apelido, máximo 40 caracteres
    elif VER == 3:
        return dado.cliente.pessoa.nome[:40]
    else:
        pass
    
def DataCasdatro(destinatario):
    return destinatario.cliente.data_cadastro

def CodigoIBGE(CIDADE_CLIENTE):
    from apps.admcore import models
    from apps.admcore.templatetags.stringsutils import normalize
    
    #CIDADE_CLIENTE = models.Endereco.objects.get(cliente=cliente).cidade
    
    IBGE = "0000000"
    
    for c in models.Cidade.objects.filter():
        if normalize(c.cidade).lower() == normalize(CIDADE_CLIENTE).lower():
            IBGE = c.codigo
    return IBGE

def TipoPessoa(cliente):
    if cliente.pessoa.tipopessoa == "F":
        return "3"
    else:
        return "1"
    
def EmissaoInicioFim(VER, EMPRESAID, DATAINICIO, DATAFIM):
    from apps.fiscal import models
    
    if VER == 1:
        return models.NotaFiscal.objects.filter(empresa_id=EMPRESAID,
                                                data_emissao__gte=DATAINICIO,
                                                data_emissao__lte=DATAFIM).order_by("data_emissao").first().data_emissao.strftime("%d/%m/%Y")
    else:
        return models.NotaFiscal.objects.filter(empresa_id=EMPRESAID,
                                                data_emissao__gte=DATAINICIO,
                                                data_emissao__lte=DATAFIM).order_by("-data_emissao").first().data_emissao.strftime("%d/%m/%Y")


NOTAS = models.NotaFiscal.objects.filter(empresa_id=EMPRESA_ID,
                                             data_emissao__gte=DATA_EMISSAO_INICIO,
                                             data_emissao__lte=DATA_EMISSAO_FIM).order_by("numero")
#Registro 0010
for nota in NOTAS:
    REGISTRO0010 = {"REGISTRO":"0010",
                "CPF_CNPJ":"{}".format(re.sub(r"[^\w\s]", "", nota.destinatario.cpfcnpj)),
                "NOME":"{}".format(ValidadorDados(2, nota.destinatario)),
                "APELIDO":"{}".format(ValidadorDados(3, nota.destinatario)),
                "ENDERECO":"{}".format(nota.destinatario.logradouro),
                "NUMERO":"{}".format(ValidadorDados(1, nota.destinatario.numero)),
                "COMPLEMENTO":"{}".format(ValidadorDados(1, nota.destinatario.complemento)),
                "BAIRRO":"{}".format(nota.destinatario.bairro),
                "IBGE":"{}".format(CodigoIBGE(nota.destinatario.cidade)),
                "UF":"{}".format(nota.destinatario.uf),
                "CODIGO_PAIS":"1058",
                "CEP":"{}".format(re.sub(r"[^\w\s]", "", nota.destinatario.cep)),
                "INSCRICAO_ESTADUAL":"",
                "INSCRICAO_MUNICIPAL":"",
                "INSCRICAO_SUFRAMA":"",
                "DDD":"",
                "TELEFONE":"",
                "FAX":"",
                "DATA_CADASTRO":"{}".format(DataCasdatro(models.NFDestinatario.objects.get(id=nota.destinatario_id)).strftime("%d/%m/%Y")),
                "CONTA_CONTABIL":"",
                "CONTA_CONTABIL_FORNECEDOR":"",
                "CLIENTE_AGRO":"N",
                "NATUREZA_JURIDICA":"7",
                "REGIME_APURACAO":"N",
                "CONTRIBUINTE_ICMS":"N",
                "ALIQUOTA_ICMS":"",
                "CATEGORIA_ESTABELECIMENTO":"",
                "INDEPENDENCIA_EMPRESA":"N",
                "PERCENTUAL_CARGA_MEDIA_MT":"",
                "PROGRAMA_AQUISAO_ALIMENTO":"N",
                "TIPO_INSCRICAO":"",
                "PROCESSO_ADMINISTRATIVO_JUDICIAL":""}
    
    print "|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(REGISTRO0010["REGISTRO"],
                                                                                                                    REGISTRO0010["CPF_CNPJ"],
                                                                                                                    REGISTRO0010["NOME"],
                                                                                                                    REGISTRO0010["APELIDO"],
                                                                                                                    REGISTRO0010["ENDERECO"],
                                                                                                                    REGISTRO0010["NUMERO"],
                                                                                                                    REGISTRO0010["COMPLEMENTO"],
                                                                                                                    REGISTRO0010["BAIRRO"],
                                                                                                                    REGISTRO0010["IBGE"],
                                                                                                                    REGISTRO0010["UF"],
                                                                                                                    REGISTRO0010["CODIGO_PAIS"],
                                                                                                                    REGISTRO0010["CEP"],
                                                                                                                    REGISTRO0010["INSCRICAO_ESTADUAL"],
                                                                                                                    REGISTRO0010["INSCRICAO_MUNICIPAL"],
                                                                                                                    REGISTRO0010["INSCRICAO_SUFRAMA"],
                                                                                                                    REGISTRO0010["DDD"],
                                                                                                                    REGISTRO0010["TELEFONE"],
                                                                                                                    REGISTRO0010["FAX"],
                                                                                                                    REGISTRO0010["DATA_CADASTRO"],
                                                                                                                    REGISTRO0010["CONTA_CONTABIL"],
                                                                                                                    REGISTRO0010["CONTA_CONTABIL_FORNECEDOR"],
                                                                                                                    REGISTRO0010["CLIENTE_AGRO"],
                                                                                                                    REGISTRO0010["NATUREZA_JURIDICA"],
                                                                                                                    REGISTRO0010["REGIME_APURACAO"],
                                                                                                                    REGISTRO0010["CONTRIBUINTE_ICMS"],
                                                                                                                    REGISTRO0010["ALIQUOTA_ICMS"],
                                                                                                                    REGISTRO0010["CATEGORIA_ESTABELECIMENTO"],
                                                                                                                    REGISTRO0010["INDEPENDENCIA_EMPRESA"],
                                                                                                                    REGISTRO0010["PERCENTUAL_CARGA_MEDIA_MT"],
                                                                                                                    REGISTRO0010["PROGRAMA_AQUISAO_ALIMENTO"],
                                                                                                                    REGISTRO0010["TIPO_INSCRICAO"],
                                                                                                                    REGISTRO0010["PROCESSO_ADMINISTRATIVO_JUDICIAL"])
    
#Registros 2000, 2020 e 2081

for nota in NOTAS:
    REGISTRO2000 = {"REGISTRO":"2000",
                    "CODIGO_ESPECIE":"{}".format(nota.modelo),
                    "CPF_CNPJ":"{}".format(re.sub(r"[^\w\s]", "", nota.destinatario.cpfcnpj)),
                    "CODIGO_ACUMULADOR":"926",
                    "CFOP":"{}".format(nota.cfop.cfop),
                    "CODIGO_EXCLUSAO_DIEF":"",
                    "UF_CLIENTE":"{}".format(nota.destinatario.uf),
                    "SEGMENTO":"",
                    "NUMERO_NOTA":"{}".format(nota.numero),
                    "SERIE_NOTA":"{}".format(nota.serie),
                    "DOCUMENTO_FINAL":"",
                    "DATA_SAIDA":"{}".format(nota.data_emissao.strftime("%d/%m/%Y")),
                    "DATA_EMISSAO":"{}".format(nota.data_emissao.strftime("%d/%m/%Y")),
                    "VALOR_CONTABIL":"{}".format(str(nota.valortotal).replace('.',',')),
                    "VALOR_EXCLUSAO_DIEF":"",
                    "OBSERVACAO":"",
                    "IBGE":"{}".format(CodigoIBGE(nota.destinatario.cidade)),
                    "MODALIDADE_FRETE":"",
                    "CFOP_ESTENDIDO":"",
                    "CODIGO_TRANSF_CREDITO":"",
                    "CODIGO_OBSERVACAO":"",
                    "DATA_VISTO_NF_TRANSF_CREDITO":"",
                    "CODIGO_ANTECIP_TRIBUB":"",
                    "FATO_GERADOR_CRF":"",
                    "FATO_GERADOR_COSIRF":"",
                    "FATO_GERADOR_IRRFP":"",
                    "TIPO_RECEITA":"1",
                    "VALOR_FRETE":"",
                    "VALOR_SEGURO":"",
                    "VALOR_DESPESAS_ACESSORIAS":"",
                    "VALOR_PRODUTOS":"{}".format(str(nota.valortotal).replace('.',',')),
                    "VALOR_BC_ICMS_ST":"0",
                    "OUTRAS_SAIDAS":"",
                    "OUTRAS_ISENTAS":"",
                    "SAIDAS_ISENTAS_CUPOM":"",
                    "SAIDAS_ISENTAS_NF_M02":"",
                    "CODIGO_MODELO_DOC_FISCAL":"",
                    "CODIGO_F_PREST_SERVICO":"",
                    "CODIGO_SIT_TRIBU":"",
                    "SUB_SERIE":"",
                    "TIPO_TITULO":"",
                    "IDEN_TITULO":"",
                    "INSCRI_ESTADUAL":"",
                    "INSCRI_MUNICIPAL":"",
                    "CHAVE_NFE":"",
                    "CODIGO_RECOLHI_FETHAB":"",
                    "RESPON_RECOLHI_FETHAB":"",
                    "TIPO_CTE":"",
                    "CTE_REF":"",
                    "CODIGO_INFO_COMPLEMENTAR":"",
                    "INFO_COMPLEMENTARES":"",
                    "CST_PIS_COFINS":"",
                    "NATUREZA_RECEITA":"",
                    "VALOR_SERVICO_PIS_COFINS":"",
                    "BC_PIS_COFINS":"",
                    "ALIQ_PIS":"0,00",
                    "ALIQ_COFINS":"0,00",
                    "QUANT_KWH":"",
                    "CST_IPI":"",
                    "TIPO_ASSINANTE":"{}".format(TipoPessoa(nota.destinatario.cliente)),
                    "TIPO_CRED_ACUM":"",
                    "LANC_SCP":"",
                    "PERIODO_PREST_SERV":"{}".format(nota.data_emissao.strftime("%m/%Y")),
                    "DATA_INIC_PREST_SERV":"{}".format(EmissaoInicioFim(1, EMPRESA_ID, DATA_EMISSAO_INICIO, DATA_EMISSAO_FIM)),
                    "DATA_FINA_PREST_SERV":"{}".format(EmissaoInicioFim(2, EMPRESA_ID, DATA_EMISSAO_INICIO, DATA_EMISSAO_FIM)),
                    "TIPO_SERV":"",
                    "EMITENTE":"P",
                    "PEDAGIO":"0,00",
                    "IPI":"",
                    "ICMS_ST":"",
                    "CLASSI_SERV_PREST":"",
                    "TIPO_ATENDIMENTO":"",
                    "CONSUM_FINAL":"",
                    "CLASSI_SERV_PREST_INDI":"",
                    "ICMS_DESONERADO":"",
                    "IPI_DEV":""}
    
    
    REGISTRO2020 = {"REGISTRO":"2020",
                    "CODIGO_IMPOSTO":"1",
                    "PERCE_RED_BC":"0",
                    "BC":"0,00",
                    "ALIQ":"0,00",
                    "VALOR_IMPOSTO":"0,00",
                    "VALOR_ISENTAS":"0",
                    "VALOR_OUTRAS":"{}".format(str(nota.valortotal).replace('.',',')),
                    "VALOR_CONTABIL":"{}".format(str(nota.valortotal).replace('.',',')),
                    "VALOR_NAO_TRIB":"0",
                    "VALOR_PARC_REDUZ":"0",
                    "VALOR_IPI":"0",
                    "CODIGO_RECOLHIMENTO":"",
                    "NAT_REND":""}
    
    
    REGISTRO2081 = {"REGISTRO":"2081",
                    "OP":"1",
                    "DOC":"{}".format(nota.numero),
                    "CLIENTE_FORNECEDOR":"{}".format(re.sub(r"[^\w\s]", "", nota.destinatario.cpfcnpj)),
                    "MODELO":"{}".format(nota.modelo),
                    "DATA_EMISSAO":"{}".format(nota.data_emissao.strftime("%d/%m/%Y")),
                    "SERIE":"{}".format(nota.serie),
                    "SUB_SERIE":"0",
                    "EMITENTE":"1",
                    "CHAVE_NFE_CTE_SAIDA":""}



    print "|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(REGISTRO2000["REGISTRO"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_ESPECIE"],
                                                                                                                                                                                                                                                REGISTRO2000["CPF_CNPJ"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_ACUMULADOR"],
                                                                                                                                                                                                                                                REGISTRO2000["CFOP"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_EXCLUSAO_DIEF"],
                                                                                                                                                                                                                                                REGISTRO2000["UF_CLIENTE"],
                                                                                                                                                                                                                                                REGISTRO2000["SEGMENTO"],
                                                                                                                                                                                                                                                REGISTRO2000["NUMERO_NOTA"],
                                                                                                                                                                                                                                                REGISTRO2000["SERIE_NOTA"],
                                                                                                                                                                                                                                                REGISTRO2000["DOCUMENTO_FINAL"],
                                                                                                                                                                                                                                                REGISTRO2000["DATA_SAIDA"],
                                                                                                                                                                                                                                                REGISTRO2000["DATA_EMISSAO"],
                                                                                                                                                                                                                                                REGISTRO2000["VALOR_CONTABIL"],
                                                                                                                                                                                                                                                REGISTRO2000["VALOR_EXCLUSAO_DIEF"],
                                                                                                                                                                                                                                                REGISTRO2000["OBSERVACAO"],
                                                                                                                                                                                                                                                REGISTRO2000["IBGE"],
                                                                                                                                                                                                                                                REGISTRO2000["MODALIDADE_FRETE"],
                                                                                                                                                                                                                                                REGISTRO2000["CFOP_ESTENDIDO"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_TRANSF_CREDITO"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_OBSERVACAO"],
                                                                                                                                                                                                                                                REGISTRO2000["DATA_VISTO_NF_TRANSF_CREDITO"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_ANTECIP_TRIBUB"],
                                                                                                                                                                                                                                                REGISTRO2000["FATO_GERADOR_CRF"],
                                                                                                                                                                                                                                                REGISTRO2000["FATO_GERADOR_COSIRF"],
                                                                                                                                                                                                                                                REGISTRO2000["FATO_GERADOR_IRRFP"],
                                                                                                                                                                                                                                                REGISTRO2000["TIPO_RECEITA"],
                                                                                                                                                                                                                                                REGISTRO2000["VALOR_FRETE"],
                                                                                                                                                                                                                                                REGISTRO2000["VALOR_SEGURO"],
                                                                                                                                                                                                                                                REGISTRO2000["VALOR_DESPESAS_ACESSORIAS"],
                                                                                                                                                                                                                                                REGISTRO2000["VALOR_PRODUTOS"],
                                                                                                                                                                                                                                                REGISTRO2000["VALOR_BC_ICMS_ST"],
                                                                                                                                                                                                                                                REGISTRO2000["OUTRAS_SAIDAS"],
                                                                                                                                                                                                                                                REGISTRO2000["OUTRAS_ISENTAS"],
                                                                                                                                                                                                                                                REGISTRO2000["SAIDAS_ISENTAS_CUPOM"],
                                                                                                                                                                                                                                                REGISTRO2000["SAIDAS_ISENTAS_NF_M02"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_MODELO_DOC_FISCAL"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_F_PREST_SERVICO"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_SIT_TRIBU"],
                                                                                                                                                                                                                                                REGISTRO2000["SUB_SERIE"],
                                                                                                                                                                                                                                                REGISTRO2000["TIPO_TITULO"],
                                                                                                                                                                                                                                                REGISTRO2000["IDEN_TITULO"],
                                                                                                                                                                                                                                                REGISTRO2000["INSCRI_ESTADUAL"],
                                                                                                                                                                                                                                                REGISTRO2000["INSCRI_MUNICIPAL"],
                                                                                                                                                                                                                                                REGISTRO2000["CHAVE_NFE"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_RECOLHI_FETHAB"],
                                                                                                                                                                                                                                                REGISTRO2000["RESPON_RECOLHI_FETHAB"],
                                                                                                                                                                                                                                                REGISTRO2000["TIPO_CTE"],
                                                                                                                                                                                                                                                REGISTRO2000["CTE_REF"],
                                                                                                                                                                                                                                                REGISTRO2000["CODIGO_INFO_COMPLEMENTAR"],
                                                                                                                                                                                                                                                REGISTRO2000["INFO_COMPLEMENTARES"],
                                                                                                                                                                                                                                                REGISTRO2000["CST_PIS_COFINS"],
                                                                                                                                                                                                                                                REGISTRO2000["NATUREZA_RECEITA"],
                                                                                                                                                                                                                                                REGISTRO2000["VALOR_SERVICO_PIS_COFINS"],
                                                                                                                                                                                                                                                REGISTRO2000["BC_PIS_COFINS"],
                                                                                                                                                                                                                                                REGISTRO2000["ALIQ_PIS"],
                                                                                                                                                                                                                                                REGISTRO2000["ALIQ_COFINS"],
                                                                                                                                                                                                                                                REGISTRO2000["QUANT_KWH"],
                                                                                                                                                                                                                                                REGISTRO2000["CST_IPI"],
                                                                                                                                                                                                                                                REGISTRO2000["TIPO_ASSINANTE"],
                                                                                                                                                                                                                                                REGISTRO2000["TIPO_CRED_ACUM"],
                                                                                                                                                                                                                                                REGISTRO2000["LANC_SCP"],
                                                                                                                                                                                                                                                REGISTRO2000["PERIODO_PREST_SERV"],
                                                                                                                                                                                                                                                REGISTRO2000["DATA_INIC_PREST_SERV"],
                                                                                                                                                                                                                                                REGISTRO2000["DATA_FINA_PREST_SERV"],
                                                                                                                                                                                                                                                REGISTRO2000["TIPO_SERV"],
                                                                                                                                                                                                                                                REGISTRO2000["EMITENTE"],
                                                                                                                                                                                                                                                REGISTRO2000["PEDAGIO"],
                                                                                                                                                                                                                                                REGISTRO2000["IPI"],
                                                                                                                                                                                                                                                REGISTRO2000["ICMS_ST"],
                                                                                                                                                                                                                                                REGISTRO2000["CLASSI_SERV_PREST"],
                                                                                                                                                                                                                                                REGISTRO2000["TIPO_ATENDIMENTO"],
                                                                                                                                                                                                                                                REGISTRO2000["CONSUM_FINAL"],
                                                                                                                                                                                                                                                REGISTRO2000["CLASSI_SERV_PREST_INDI"],
                                                                                                                                                                                                                                                REGISTRO2000["ICMS_DESONERADO"],
                                                                                                                                                                                                                                                REGISTRO2000["IPI_DEV"])
    
    print "|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(REGISTRO2020["REGISTRO"],
                                                            REGISTRO2020["CODIGO_IMPOSTO"],
                                                            REGISTRO2020["PERCE_RED_BC"],
                                                            REGISTRO2020["BC"],
                                                            REGISTRO2020["ALIQ"],
                                                            REGISTRO2020["VALOR_IMPOSTO"],
                                                            REGISTRO2020["VALOR_ISENTAS"],
                                                            REGISTRO2020["VALOR_OUTRAS"],
                                                            REGISTRO2020["VALOR_CONTABIL"],
                                                            REGISTRO2020["VALOR_NAO_TRIB"],
                                                            REGISTRO2020["VALOR_PARC_REDUZ"],
                                                            REGISTRO2020["VALOR_IPI"],
                                                            REGISTRO2020["CODIGO_RECOLHIMENTO"],
                                                            REGISTRO2020["NAT_REND"])

    print "|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(REGISTRO2081["REGISTRO"],
                                                REGISTRO2081["OP"],
                                                REGISTRO2081["DOC"],
                                                REGISTRO2081["CLIENTE_FORNECEDOR"],
                                                REGISTRO2081["MODELO"],
                                                REGISTRO2081["DATA_EMISSAO"],
                                                REGISTRO2081["SERIE"],
                                                REGISTRO2081["SUB_SERIE"],
                                                REGISTRO2081["EMITENTE"],
                                                REGISTRO2081["CHAVE_NFE_CTE_SAIDA"])