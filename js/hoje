const lista =
    document.getElementById("listaAniversariantes");

const formPesquisa =
    document.getElementById("formPesquisa");

const mensagemErro =
    document.getElementById("mensagemErro");



function mostrarErro(mensagem) {

    mensagemErro.textContent = mensagem;

    mensagemErro.hidden = false;
}



function criarCard(usuario) {

    return `
        <article class="usuario-card">

            <div class="usuario-info">

                <h3>
                    ${usuario.nome}
                </h3>

                <p>
                    Data de nascimento:
                    ${formatarData(usuario.data_aniversario)}
                </p>

                <p>
                    ID:
                    ${usuario.id}
                </p>

            </div>

            <div class="usuario-acoes">

                <button
                    class="botao-editar"
                    onclick="editar(${usuario.id})"
                >
                    Editar
                </button>

                <button
                    class="botao-excluir"
                    onclick="excluir(${usuario.id})"
                >
                    Excluir
                </button>

            </div>

        </article>
    `;
}



function formatarData(data) {

    const partes = data.split("-");

    return `${partes[2]}/${partes[1]}/${partes[0]}`;
}



async function carregarAniversariantesHoje() {

    mensagemErro.hidden = true;

    lista.innerHTML =
        `<p class="carregando">Carregando...</p>`;


    try {

        const usuarios =
            await buscarAniversariantesDia();


        if (!usuarios.length) {

            lista.innerHTML =
                `<p>Ninguém faz aniversário hoje.</p>`;

            return;
        }


        lista.innerHTML =
            usuarios
                .map(criarCard)
                .join("");


    } catch (erro) {

        lista.innerHTML = "";

        mostrarErro(erro.message);
    }
}



async function pesquisar() {

    mensagemErro.hidden = true;


    const termo =
        document
            .getElementById("termoPesquisa")
            .value
            .trim();


    if (!termo) {

        mostrarErro(
            "Digite um nome para pesquisar."
        );

        return;
    }


    try {

        const usuarios =
            await pesquisarUsuario(termo);


        if (!usuarios.length) {

            lista.innerHTML =
                `<p>Nenhuma pessoa encontrada.</p>`;

            return;
        }


        lista.innerHTML =
            usuarios
                .map(criarCard)
                .join("");


    } catch (erro) {

        mostrarErro(erro.message);
    }
}



formPesquisa.addEventListener(
    "submit",
    function (event) {

        event.preventDefault();

        pesquisar();

    }
);



function editar(id) {

    window.location.href =
        `edicao.html?id=${id}`;
}



async function excluir(id) {

    const confirmar =
        confirm(
            "Tem certeza que deseja excluir esta pessoa?"
        );


    if (!confirmar) {

        return;
    }


    try {

        await excluirUsuario(id);


        alert(
            "Pessoa excluída com sucesso!"
        );


        carregarAniversariantesHoje();


    } catch (erro) {

        mostrarErro(erro.message);
    }
}



carregarAniversariantesHoje();
