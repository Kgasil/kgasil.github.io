# GRAAL — Code signing policy / Política de assinatura de código

## Estado atual

Responsável declarado pelo projeto: Kaio Gabriel da Silva, K&G Vision (iniciativa independente). Esta declaração não representa validação de identidade por autoridade certificadora.

- Certificado de desenvolvimento autoassinado: demonstração isolada de Authenticode em script inofensivo. A cada rodada a chave é criada no Windows de CI, não exportável, removida ao final. Nenhuma raiz de confiança é instalada. O certificado público de demonstração não deve ser instalado nem usado para aprovar aplicativos. Não é um certificado pessoal de produção, nem uma chave reutilizável do titular.
- Atestação de procedência: GitHub/Sigstore assina criptograficamente o manifesto gerado a partir dos arquivos-fonte do site. A identidade autenticada é a do workflow/repositório, não uma autoridade verificando o nome civil do autor. Não é Authenticode nem certificação antimalware.
- Aeris EXE público permanece sem assinatura comercial. Genesis/Argus Mini permanecem sob os bloqueios de distribuição existentes. Não assinar ou alterar amostras em investigação, nem substituir os pacotes atuais.
- SignPath Foundation exige licença OSI e avaliação própria. Aeris e Lilium ainda não declaram licença open source; não houve alteração de licenciamento nem solicitação ao fornecedor. A assinatura concedida pelo programa usaria a identidade da Fundação.
- Microsoft Store: assinatura de MSIX pela loja após certificação, gratuita segundo a documentação Microsoft. Cadastro, identidade, empacotamento, termos e aprovação ainda pendentes. Não confundir com assinatura do EXE externo.

## Verificação e exemplos

[Execuções](https://github.com/Kgasil/kgasil.github.io/actions/workflows/graal-signing.yml). O artefato de teste contém apenas script demonstrativo assinado, certificado público de teste e evidência JSON; nenhuma chave privada. O manifesto de procedência é verificável com GitHub CLI:

```sh
gh attestation verify graal-web-provenance.json --repo Kgasil/kgasil.github.io
```

O resultado esperado identifica o repositório e workflow, não um editor Windows verificado. Nenhuma publicação comercial é aprovada por esta automação.

Fontes: [Microsoft: opções de assinatura](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/code-signing-options) · [SignPath: condições](https://signpath.org/terms.html) · [GitHub: atestações](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations).
