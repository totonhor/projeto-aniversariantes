const formCadastro =
    document.getElementById("formCadastro");

const mensagemErro =
    document.getElementById("mensagemErro");

const mensagemSucesso =
    document.getElementById("mensagemSucesso");



formCadastro.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        mensagemErro.hidden = true;

        mensagemSucesso.hidden = true;


        const nome =
            document
                .getElementById("nome")
                .value
                .trim();


        const dataAniversario =
            document
                .getElementById("dataAniversario")
                .value;


        if (!nome || !dataAniversario) {

            mensagemErro.textContent =
                "Preencha todos os campos.";

            mensagemErro.hidden = false;

            return;
        }


        const usuario = {

            nome: nome,

            data_aniversario:
                dataAniversario

        };


        try {

            await cadastrarUsuario(
                usuario
            );


            mensagemSucesso.textContent =
                "Pessoa cadastrada com sucesso!";


            mensagemSucesso.hidden = false;


            formCadastro.reset();


        } catch (erro) {

            mensagemErro.textContent =
                erro.message;

            mensagemErro.hidden = false;
        }

    }
);
