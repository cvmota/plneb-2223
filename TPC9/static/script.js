$(document).ready(function () {
    $('#example').DataTable();
});

function deleteTerm(designation) {
    // Mostra um alerta de confirmação

    var confirmation = confirm("Are you sure you want to delete the term '" + designation + "'?" );

    // Se clicou em OK, faz o pedido de delete
    if (confirmation) {
        $.ajax("/term/" + designation, {
            type: "DELETE",
            success: function(result) {
                // Recarrega a página após a exclusão bem-sucedida
                location.reload();
                alert("Term deleted!");
            },
            error: function(xhr, status, error) {
                // Exibe uma mensagem de erro em caso de falha na exclusão
                alert("Error deleting term: " + error);
            }
        });
    }
}
