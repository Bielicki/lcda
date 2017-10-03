(function (window) {
    'use strict';

    function library() {
        var content = {};

        var $client = $('#id_client')
        var $name = $('#id_name');
        var $code = $('#id_code');
        var $email = $('#id_email');
        var $survey = $('#id_survey');
        var $contract = $('#id_contract');
        content.setup = function (url) {
            var table = $('#table').DataTable({
                responsive: true,
                order: [[0, 'asc']],
                columnDefs: [{
                    orderable: false,
                    targets: -1,
                    className: 'text-right',
                    render: function (data, type, row) {
                        return getButtons(row[4])[0].outerHTML;
                    }
                }],
                iDisplayLength: 20,
                bLengthChange: false,
                dom: 'lrt<"row"<"col-sm-6"i><"col-sm-6"p>>',
                processing: true,
                serverSide: true,
                sServerMethod: 'POST',
                ajax: {
                    url: url,
                    data: function (d) {
                        d.name = $name.val();
                        d.code = $code.val();
                        d.email = $email.val();
                        d.survey = $survey.val();
                        d.client = $client.val();
                        d.contract = $contract.val();
                    }
                }
            });

            $name.on('keyup', table.draw);
            $code.on('keyup', table.draw);
            $email.on('keyup', table.draw);
            $survey.on('keyup', table.draw);
            $client.on('keyup', table.draw);
            $contract.on('keyup', table.draw);

        };

        function getButtons(urls) {
            var $container = $('<div>', {'class': 'table-buttons'});

            var $update_button = $('<a>', {
                'class': 'btn btn-sm btn-primary icon',
                'href': urls.update_url,
                'html': $('<i>', {'class': 'fa fa-pencil'})
            });

            var $delete_button = $('<a>', {
                'class': 'btn btn-sm btn-danger icon',
                'href': urls.delete_url,
                'html': $('<i>', {'class': 'fa fa-times'})
            });

            $container.append($update_button);
            $container.append($delete_button);

            return $container;
        }

        return content;
    }

    window.CompanyListView = library();
})(window);