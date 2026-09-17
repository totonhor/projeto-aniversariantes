const parametros =
    new URLSearchParams(
        window.location.search
    );


const id =
    parametros.get("id");


const form =
    document.getElementById("formEdicao");


const mensagemErro =
    document.getElementById("mensagemErro");



async function carregarUsuario() {

    if (!id) {

        mensagemErro.textContent =
            "ID do usuário não informado.";

        mensagemErro.hidden = false;

        form.style.display = "none";

        return;
    }


    try {

        const usuarios =
            await buscarTodosUsuarios();


        const usuario =
            usuarios.find(
                pessoa =>
                    String(pessoa.id) ===
                    String(id)
            );


        if (!usuario) {

            mensagemErro.textContent =
                "Pessoa não encontrada.";

            mensagemErro.hidden = false;

            form.style.display = "none";

            return;
        }


        document.getElementById("id").value =
            usuario.id;


        document.getElementById("nome").value =
            usuario.nome;


        document.getElementById(
            "dataAniversario"
        ).value =
            usuario.data_aniversario;


    } catch (erro) {

        mensagemErro.textContent =
            erro.message;

        mensagemErro.hidden = false;
    }
}



form.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();

        mensagemErro.hidden = true;


        const nome =
            document
                .getElementById("nome")
                .value
                .trim();


        const dataAniversario =
            document
                .getElementById(
                    "dataAniversario"
                )
                .value;


        const dados = {

            nome: nome,

            data_aniversario:
                dataAniversario

        };


        try {

            await editarUsuario(
                id,
                dados
            );


            alert(
                "Alterações salvas com sucesso!"
            );


            window.location.href =
                "calendario.html";


        } catch (erro) {

            mensagemErro.textContent =
                erro.message;

            mensagemErro.hidden = false;
        }
    }
);



carregarUsuario();
