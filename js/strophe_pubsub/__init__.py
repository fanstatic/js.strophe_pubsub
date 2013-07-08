from fanstatic import Library, Resource

library = Library('strophe.pubsub.js', 'resources')

strophe_pubsub = fanstatic.Resource(
    library, 'strophe.pubsub.js', depends=[js.strophe])
