from trac.core import *
from trac.config import *
from trac.ticket.api import ITicketActionController
from trac.web.api import IRequestFilter

class WorkflowTicketFieldsModule(Component):
    implements(IRequestFilter, ITicketActionController)

    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, data, content_type):
        if template != 'ticket.html':
            return (template, data, content_type)

        fields = data.get("fields")
        if not fields:
            return (template, data, content_type)

        for field in data['fields']:
            if field['name'] in ("milestone", "version", "reporter"):
                field['skip'] = True
        return (template, data, content_type)
