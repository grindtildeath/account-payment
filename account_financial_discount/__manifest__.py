# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Account financial discount",
    "version": "14.0.1.0.0",
    "category": "Account",
    "website": "https://github.com/OCA/account-payment",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["account"],
    "data": [
        "views/payment_term_form.xml",
        "views/account_move.xml",
        "views/account_payment.xml",
        "views/account_reconcile_model.xml",
        "views/res_config_settings.xml",
        "views/payment_receipt.xml",
    ],
}
