const nomeMes =
    document.getElementById("nomeMes");

const diasCalendario =
    document.getElementById("diasCalendario");

const lista =
    document.getElementById("listaAniversariantes");

const mensagemErro =
    document.getElementById("mensagemErro");

const mesAnterior =
    document.getElementById("mesAnterior");

const mesProximo =
    document.getElementById("mesProximo");

const formPesquisa =
    document.getElementById("formPesquisa");


const nomesMeses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
];


let mesAtual =
    new Date().getMonth() + 1;



function mostrarErro(mensagem) {

    mensagemErro.textContent = mensagem;

    mensagemErro.hidden = false;
}



function formatarData(data) {

    const partes = data.split("-");

    return `${partes[2]}/${partes[1]}/${partes[0]}`;
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



function criarCalendario(usuarios) {

    diasCalendario.innerHTML = "";


    const ano =
        new Date().getFullYear();


    const primeiroDia =
        new Date(
            ano,
            mesAtual - 1,
            1
        ).getDay();


    const quantidadeDias =
        new Date(
            ano,
            mesAtual,
            0
        ).getDate();


    for (
        let i = 0;
        i < primeiroDia;
        i++
    ) {

        const vazio =
            document.createElement("div");

        vazio.className =
            "dia vazio";

        diasCalendario.appendChild(vazio);
    }


    for (
        let dia = 1;
        dia <= quantidadeDias;
        dia++
    ) {

        const elemento =
            document.createElement("div");

        elemento.className =
            "dia";


        const numero =
            document.createElement("span");

        numero.className =
            "numero-dia";

        numero.textContent =
            dia;


        elemento.appendChild(numero);


        const aniversariantes =
            usuarios.filter(
                usuario => {

                    const partes =
                        usuario.data_aniversario
                            .split("-");

                    return (
                        Number(partes[2]) === dia
                    );
                }
            );


        aniversariantes.forEach(
            usuario => {

                const aniversario =
                    document.createElement("span");

                aniversario.className =
                    "aniversario";

                aniversario.textContent =
                    usuario.nome;

                elemento.appendChild(
                    aniversario
                );
            }
        );


        diasCalendario.appendChild(
            elemento
        );
    }
}



async function carregarMes() {

    mensagemErro.hidden = true;

    nomeMes.textContent =
        nomesMeses[mesAtual - 1];


    lista.innerHTML =
        `<p class="carregando">Carregando...</p>`;


    try {

        const usuarios =
            await buscarAniversariantesMes(
                mesAtual
            );


        criarCalendario(usuarios);


        if (!usuarios.length) {

            lista.innerHTML =
                `<p>Nenhum aniversariante neste mês.</p>`;

            return;
        }


        lista.innerHTML =
            usuarios
                .map(criarCard)
                .join("");


    } catch (erro) {

        diasCalendario.innerHTML = "";

        lista.innerHTML = "";

        mostrarErro(erro.message);
    }
}



mesAnterior.addEventListener(
    "click",
    function () {

        mesAtual--;

        if (mesAtual < 1) {

            mesAtual = 12;
        }

        carregarMes();
    }
);



mesProximo.addEventListener(
    "click",
    function () {

        mesAtual++;

        if (mesAtual > 12) {

            mesAtual = 1;
        }

        carregarMes();
    }
);



formPesquisa.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();

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


        carregarMes();


    } catch (erro) {

        mostrarErro(erro.message);
    }
}



carregarMes();
