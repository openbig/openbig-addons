# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
#    Module base_apps_menu_invisible for OpenERP                                #
#    Copyrigt (C) 2013 OpenGLOBE Grzegorz Grzelak (www.openglobe.pl)            #
#                       and big-consulting GmbH (www.openbig.de)                #
#                                                                               #
#    This program is free software: you can redistribute it and/or modify       #
#    it under the terms of the GNU Affero General Public License as             #
#    published by the Free Software Foundation, either version 3 of the         #
#    License, or (at your option) any later version.                            #
#                                                                               #
#    This program is distributed in the hope that it will be useful,            #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#    GNU Affero General Public License for more details.                        #
#                                                                               #
#    You should have received a copy of the GNU Affero General Public License   #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                               #
#################################################################################

from openerp.osv import osv
import logging

_logger = logging.getLogger(__name__)

class publisher_warranty_contract(osv.osv):
    _inherit = 'publisher_warranty.contract'

    def update_notification(self, cr, uid, ids, cron_mode=True,
                            context=None):

        #_logger.info("NO More Spying Stuff")

        return True


publisher_warranty_contract()

