# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    Module openbig_customize
#    Copyrigt (C) 2010 OpenGLOBE Andrzej Grymkowski (www.openglobe.pl)
#                       and big-consulting GmbH (www.openbig.org)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time

from openerp.report import report_sxw

class order(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(order, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time, 
            'show_discount':self._show_discount,
            'display_addressOB': self.display_addressOB,
            'get_partner_name': self.get_partner_name,
            'get_partner': self.get_partner,
        })

    def _show_discount(self, uid, context=None):
        cr = self.cr
        try: 
            group_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'sale', 'group_discount_per_so_line')[1]
        except:
            return False
        return group_id in [x.id for x in self.pool.get('res.users').browse(cr, uid, uid, context=context).groups_id]

    def get_partner(self, partner, type):
        partner_pool = self.pool.get('res.partner')
        partner_id = partner_pool.address_get(self.cr, self.uid, [partner.id], [type])

        if partner_id and partner_id.get(type, None):
            return partner_pool.browse(self.cr, self.uid, partner_id.get(type), context=self.localcontext)
        return None
        
    def get_partner_name(self, partner):
        if not partner:
            return ''
        title = ''
        if partner.title:
            title = partner.title.name+ ' '
        return u'%s%s' % (title, partner.name)

        
    # copy/paste from base/res_partner.py
    def display_addressOB(self, address):
        if not address:
            return ''
        return self.pool.get('res.partner')._display_address(self.cr, self.uid, address, without_company=True)


report_sxw.report_sxw('report.sale.order.orderreport', 'sale.order', 'addons/openbig_customize/report/sale_order_orderreport.rml', parser=order, header="external")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
