from events.models import Event


class NextEventMixin(object):

    def _get_next_event(self):
        try:
            return Event.objects.next_event()
        except Event.DoesNotExist:
            return None
