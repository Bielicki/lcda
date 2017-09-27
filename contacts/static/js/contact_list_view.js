(function (window) {
    'use strict';

    function library() {
        var content = {};

        var $name = $('#id_name');
        var $surname = $('#id_surname');
        var $email = $('#id_email');
        var $company = $('#id_company');
        var $survey = $('#id_survey');
        var $location = $('#id_location');
        content.setup = function (url) {
            var table = $('#table').DataTable({
                responsive: true,
                order: [[0, 'asc']],
                columnDefs: [{
                    orderable: false,
                    targets: -1,
                    className: 'text-right',
                    render: function (data, type, row) {
                        return getButtons(row[8])[0].outerHTML;
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
                        d.surname = $surname.val();
                        d.email = $email.val();
                        d.company = $company.val();
                        d.survey = $survey.val();
                        d.location = $location.val();
                    }
                }
            });

            $name.on('keyup', table.draw);
            $surname.on('keyup', table.draw);
            $email.on('keyup', table.draw);
            $company.on('keyup', table.draw);
            $survey.on('keyup', table.draw);
            $location.on('keyup', table.draw);
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

    window.ContactListView = library();
})(window);