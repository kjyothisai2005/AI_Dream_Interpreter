# # # dream_interpreter/nlp_module.py

# # import spacy
# # from textblob import TextBlob

# # # Load spaCy English model
# # nlp = spacy.load("en_core_web_sm")

# # # Example symbolic map (extend this)
# # symbol_dict = {
# #     "snake": {
# #         "freud": "repressed sexuality or danger",
# #         "jung": "transformation or unconscious fears"
# #     },
# #     "water": {
# #         "freud": "birth or unconscious mind",
# #         "jung": "emotions or the unknown"
# #     },
# #     "falling": {
# #         "freud": "loss of control",
# #         "jung": "failure or grounding"
# #     }
# # }

# # def extract_symbols(text):
# #     doc = nlp(text.lower())
# #     keywords = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'PROPN']]
# #     matched_symbols = {k: v for k, v in symbol_dict.items() if k in keywords}
# #     return matched_symbols

# # def detect_emotion(text):
# #     analysis = TextBlob(text)
# #     polarity = analysis.sentiment.polarity
# #     if polarity > 0.3:
# #         return "positive"
# #     elif polarity < -0.3:
# #         return "negative"
# #     else:
# #         return "neutral"

# # def interpret_dream(text):
# #     symbols = extract_symbols(text)
# #     emotion = detect_emotion(text)
# #     interpretation = []

# #     for symbol, theories in symbols.items():
# #         interpretation.append(f"Symbol: **{symbol}**")
# #         for theory, meaning in theories.items():
# #             interpretation.append(f" - {theory.capitalize()} Interpretation: {meaning}")
# #     interpretation.append(f"\nOverall emotional tone: **{emotion}**")
    
# #     return "\n".join(interpretation), list(symbols.keys()), emotion
# import spacy
# from textblob import TextBlob

# nlp = spacy.load("en_core_web_sm")

# symbol_dict = {
#     "snake": {"freud": "repressed danger, primal instincts", "jung": "transformation or unconscious fears"},
#     "water": {"freud": "birth or unconscious mind", "jung": "emotions or the unknown"},
#     "falling": {"freud": "loss of control, anxiety", "jung": "failure or grounding"},
#     "fire": {"freud": "intense emotions, aggression, or destruction", "jung": "purification or transformation"},
#     "freedom": {"freud": "desire for liberation from constraints or responsibility", "jung": "self-actualization or transcendence"},
#     "fear": {"freud": "repressed anxiety or unresolved conflicts", "jung": "shadow archetype or unknown"},
#     "death": {"freud": "fear of loss, guilt, or the end of a phase", "jung": "transformation or the ego’s dissolution"},
#     "flying": {"freud": "desire for liberation from constraints, escape from reality", "jung": "spiritual elevation or escape from reality"},
#     "teeth": {"freud": "vulnerability, fear of aging, or aggression", "jung": "loss of power or personal transition"},
#     "baby": {"freud": "desire for new beginnings or unresolved childhood issues", "jung": "new beginnings or undeveloped potential"},
#     "house": {"freud": "the self, security, or compartments of the mind", "jung": "the psyche or mind (rooms as aspects of personality)"},
#     "mirror": {"freud": "self-perception, vanity, or introspection", "jung": "confronting the true self or persona"},
#     "blood": {"freud": "life force, vitality, or trauma", "jung": "sacrifice or deep emotional pain"},
#     "train": {"freud": "life's journey, fixed path, or unconscious drives", "jung": "destiny or personal journey"},
#     "spider": {"freud": "overpowering figure, entrapment, or anxiety", "jung": "creation or the shadow aspect"},
#     "darkness": {"freud": "fear of the unknown, suppressed desires, or the unconscious", "jung": "the unconscious or shadow self"},
#     "stairs": {"freud": "progress, ascent/descent in consciousness, or transition", "jung": "movement through consciousness levels"},
#     "school": {"freud": "performance anxiety, authority issues, or learning experiences", "jung": "life lessons or inner development"},
#     "car": {"freud": "control or power over direction, personal drive", "jung": "ego-driven choices or life’s path"},
#     "door": {"freud": "opportunity, transition, or hidden aspects", "jung": "transition or threshold to new self"},
#     "forest": {
#         "freud": "repressed desires hidden in the subconscious, the unknown aspects of self",
#         "jung": "the unknown, exploration of the unconscious"
#     },
#     "mountain": {
#         "freud": "challenge to overcome, ambition, or an obstacle",
#         "jung": "aspiration, spiritual growth, or inner journey"
#     },
#     "clock": {
#         "freud": "anxiety about aging, time running out, or urgency",
#         "jung": "awareness of life's cycle or personal timing"
#     },
#     "phone": {
#         "freud": "desire for communication, intimacy, or connection",
#         "jung": "connection to unconscious messages or intuition"
#     },
#     "glass": {
#         "freud": "fragility, transparency, or barriers in relationships",
#         "jung": "clarity or the boundary between self and others"
#     },
#     "clown": {
#         "freud": "repressed fear masked by humor, hidden aspects of personality",
#         "jung": "the trickster archetype or hidden emotions"
#     },
#     "phone call": {
#         "freud": "desire for attention, fear of news, or communication needs",
#         "jung": "message from the unconscious"
#     },
#     "bridge": {
#         "freud": "transition, connection between states or ideas, or overcoming a divide",
#         "jung": "connection between conscious and unconscious"
#     },
#     "tornado": {
#         "freud": "emotional upheaval, inner chaos, or destructive urges",
#         "jung": "a powerful force of transformation"
#     },
#     "shadow": {
#         "freud": "repressed urges, guilt, or unconscious aspects of personality",
#         "jung": "the 'shadow self'—parts of psyche not accepted by ego"
#     },
#     "animals": {
#         "freud": "instinctual drives, untamed desires, or primal nature",
#         "jung": "primal archetypes or spirit guides"
#     },
#     "money": {
#         "freud": "power, control, security, or self-worth issues",
#         "jung": "self-worth or energy exchange"
#     },
#     "injury": {
#         "freud": "fear of punishment, guilt, or psychological wounds",
#         "jung": "symbol of vulnerability or personal sacrifice"
#     },
#     "eye": {
#         "freud": "voyeurism, being watched, or awareness",
#         "jung": "awareness, insight, or spiritual vision"
#     },
#     "hair": {
#         "freud": "identity, strength, vanity, or a desire to be seen",
#         "jung": "identity, strength, or vanity"
#     },
#     "shoes": {
#         "freud": "personal path, grounding, or a desire for stability",
#         "jung": "life path or grounding"
#     },
#     "keys": {
#         "freud": "hidden access, control, or unlocking secrets",
#         "jung": "unlocking potential or mysteries of the psyche"
#     },
#     "window": {
#         "freud": "desire for freedom, escape, or a view into inner/outer world",
#         "jung": "vision or barrier between worlds"
#     },
#     "jewelry": {
#         "freud": "vanity, materialism, emotional attachment, or perceived value",
#         "jung": "personal value or spiritual treasure"
#     },
#     "room": {
#         "freud": "personal secrets, compartments of self, or aspects of identity",
#         "jung": "segments of the psyche or hidden memories"
#     },
#     "clothing": {
#         "freud": "modesty, self-presentation, shame, or hidden aspects",
#         "jung": "persona or social mask"
#     },
#     "colors": {
#         "freud": "emotional associations from early experiences, mood, or repressed feelings",
#         "jung": "symbolic archetypes tied to universal themes"
#     },
#     "desert": {
#         "freud": "isolation, emotional emptiness, or desolation",
#         "jung": "testing ground for spiritual transformation"
#     },
#     "ocean": {
#         "freud": "overwhelming unconscious desires, maternal influence, or vast emotions",
#         "jung": "collective unconscious or deep emotion"
#     },
#     "mask": {
#         "freud": "repression, desire to hide, or false self",
#         "jung": "persona or false identity"
#     },
#     "road": {
#         "freud": "life's direction, personal journey, or an inevitable path",
#         "jung": "path to individuation or spiritual progress"
#     },
#     "robot": {
#         "freud": "loss of emotion, feeling mechanized, or control issues",
#         "jung": "disconnection from the soul or self-alienation"
#     },
#     "child": {
#         "freud": "unresolved childhood desires, regression, or innocence",
#         "jung": "inner child or potential for growth"
#     },
#     "angel": {
#         "freud": "idealized superego, moral authority, or a desire for protection",
#         "jung": "messenger from the higher self or divine guidance"
#     },
#     "storm": {
#         "freud": "repressed aggression, emotional upheaval, or conflict",
#         "jung": "inner conflict or cathartic transformation"
#     },
#     "books": {
#         "freud": "desire for knowledge, authority, or escape through fantasy",
#         "jung": "hidden wisdom or spiritual learning"
#     },
#     "garden": {
#         "freud": "nurturing, hidden pleasures, or a controlled environment of desires",
#         "jung": "the psyche's inner sanctuary, growth, or potential"
#     },
#     "river": {
#         "freud": "flow of life energy, emotional currents, or unstoppable forces",
#         "jung": "the journey of life, transformation, or emotional flow"
#     },
#     "bird": {
#         "freud": "desire for freedom, transcendence, or communication",
#         "jung": "spirit, transcendence, or communication"
#     },
#     "tree": {
#         "freud": "growth, connection to family roots, or stability",
#         "jung": "growth, wisdom, connection to nature, or the self"
#     },
#     "castle": {
#         "freud": "ego defense, protection of secrets, or desire for power and security",
#         "jung": "the self, a place of spiritual refuge, or the collective unconscious"
#     },
#     "sun": {
#         "freud": "conscious ego, male energy, or desire for recognition",
#         "jung": "the self, consciousness, vitality, or masculine principle"
#     },
#     "moon": {
#         "freud": "feminine principle, the unconscious, or maternal influence",
#         "jung": "the anima, intuition, cycles, or the unconscious"
#     },
#     "boat": {
#         "freud": "journey through life, exploration of emotions, or escape",
#         "jung": "journey across the unconscious, exploration of emotions, or transition"
#     },
#     "crown": {
#         "freud": "desire for power, control, or superiority",
#         "jung": "authority, self-mastery, spiritual attainment, or wholeness"
#     },
#     "food": {
#         "freud": "primal needs, gratification, or nurturing",
#         "jung": "nourishment for the soul, psychological sustenance, or transformation"
#     },
#     "light": {
#         "freud": "enlightenment, revelation of repressed thoughts, or intellectual clarity",
#         "jung": "consciousness, spiritual insight, divine revelation, or illumination"
#     },
#     "cave": {
#         "freud": "the unconscious mind, hidden desires, or a place of retreat",
#         "jung": "initiation, spiritual retreat, the dwelling of the unconscious, or a place of rebirth"
#     },
#     "gift": {
#         "freud": "desire for reciprocation, hidden debt, or a gesture of affection",
#         "jung": "latent potential, recognition of worth, or a blessing from the unconscious"
#     },
#     "prison": {
#         "freud": "repression, guilt, or feeling trapped by inner conflicts",
#         "jung": "restriction of the self, inner limitations, or a period of necessary isolation"
#     },
#     "weapon": {
#         "freud": "aggression, defense mechanisms, or a means of control",
#         "jung": "power, ability to assert oneself, defense against the shadow, or self-destruction"
#     },
#     "music": {
#         "freud": "expression of raw emotion, unresolved feelings, or comfort",
#         "jung": "the harmonious union of opposites, expression of the soul, or access to the collective unconscious"
#     },
#     "dance": {
#         "freud": "liberated energy, unconscious urges, or a playful release of tension",
#         "jung": "rhythmic expression of life, integration of body and spirit, or a ritualistic connection to the archetypes"
#     },
#     "wall": {
#         "freud": "emotional barriers, resistance to change, or defense against anxiety",
#         "jung": "boundaries, protection of the ego, or an obstacle to individuation"
#     },
#     "map": {
#         "freud": "desire for control, planning, or a guide to psychological territories",
#         "jung": "a guide to the self, life's journey, or a plan for personal evolution"
#     },
#     "gate": {
#         "freud": "access to new experiences, a point of decision, or a boundary",
#         "jung": "transition, a threshold to a new stage of consciousness, or passage to the sacred"
#     },
#     "farm": {
#         "freud": "fertility, primal needs, or a return to simpler existence",
#         "jung": "nurturing the self, cultivating inner resources, or grounding in reality"
#     },
#     "well": {
#         "freud": "source of desires, hidden emotional depths, or a place of nourishment",
#         "jung": "the unconscious source of life, wisdom, or intuition"
#     },
#     "laboratory": {
#         "freud": "experimentation, control, or intellectual exploration of inner processes",
#         "jung": "a place of inner transformation, self-analysis, or the conscious working with unconscious material"
#     },
#     "city": {
#         "freud": "society's influence, structured life, or collective anxieties",
#         "jung": "the collective, structured consciousness, or the ego's external world"
#     },
#     "countryside": {
#         "freud": "return to nature, primal instincts, or escape from societal pressures",
#         "jung": "the unconscious, a state of natural being, simplicity, or spiritual renewal"
#     },
#     "voice": {
#         "freud": "expression of hidden desires, internal monologue, or influential figures",
#         "jung": "inner guidance, archetypal communication, or the authentic self's expression"
#     },
#     "hand": {
#         "freud": "agency, skill, connection, or control",
#         "jung": "action, creativity, connection, or the conscious ability to shape one's destiny"
#     },
#     "chains": {
#         "freud": "bondage, repression of desires, or feeling trapped by inner conflicts",
#         "jung": "limitations, unacknowledged complexes, or self-imposed restrictions that need to be broken"
#     },
#     "fireplace": {
#         "freud": "warmth, comfort, contained passion, or a central point of the home",
#         "jung": "the hearth, warmth of the inner self, transformation of raw energy, or spiritual center"
#     },
#     "vortex": {
#         "freud": "overwhelming emotions, chaos, or a loss of control",
#         "jung": "a powerful force of transformation, a gateway to other realms of consciousness, or intense psychic energy"
#     },
#     "star": {
#         "freud": "aspirations, distant hopes, or idealized figures",
#         "jung": "guidance, destiny, higher self, or divine connection"
#     },
#     "cloud": {
#         "freud": "obscurity, confusion, repressed thoughts, or fleeting anxieties",
#         "jung": "unformed thoughts, potential, mystery, or the unconscious"
#     },
#     "rain": {
#         "freud": "emotional release, sadness, cleansing, or early childhood experiences",
#         "jung": "purification, emotional release, renewal, or grace"
#     },
#     "wind": {
#         "freud": "unseen forces, emotional changes, or external pressures",
#         "jung": "spirit, creative energy, change, or fate"
#     },
#     "flower": {
#         "freud": "beauty, fragility, growth, or a fleeting pleasure",
#         "jung": "growth, beauty, spirit, or the development of the self"
#     },
#     "wolf": {
#         "freud": "aggression, primal instincts, or a feared figure",
#         "jung": "instinct, wildness, shadow archetype, or loyalty"
#     },
#     "egg": {
#         "freud": "potential, fragility, or early development",
#         "jung": "birth, new beginnings, wholeness, or untapped potential"
#     },
#     "nest": {
#         "freud": "security, comfort, early dependence, or a desire for retreat",
#         "jung": "home, security, nurturing, or a place of growth"
#     },
#     "island": {
#         "freud": "isolation, self-sufficiency, or a retreat from reality",
#         "jung": "individuation, inner sanctuary, or a place of self-discovery"
#     },
#     "volcano": {
#         "freud": "repressed anger, explosive emotions, or uncontrolled urges",
#         "jung": "release of intense energy, transformation, or profound emotional upheaval"
#     },
#     "waterfall": {
#         "freud": "overwhelming emotions, unstoppable forces, or a release of tension",
#         "jung": "flow of life, emotional catharsis, cleansing, or spiritual abundance"
#     },
#     "lake": {
#         "freud": "stillness, hidden emotions, or a tranquil but deep unconscious",
#         "jung": "the unconscious mind, reflection, depth, or emotional tranquility"
#     },
#     "valley": {
#         "freud": "a low point, depression, or a protected space",
#         "jung": "humility, introspection, sheltered growth, or a period of rest"
#     },
#     "bee": {
#         "freud": "busy activity, social pressure, or anxiety about productivity",
#         "jung": "industry, community, order, or focused energy"
#     },
#     "butterfly": {
#         "freud": "transformation, fleeting beauty, or a desire for lightness",
#         "jung": "transformation, rebirth, spiritual evolution, or the soul"
#     },
#     "anchor": {
#         "freud": "security, stability, feeling tied down, or a need for grounding",
#         "jung": "stability, hope, security, or grounding"
#     },
#     "rope": {
#         "freud": "connection, entanglement, constraint, or a lifeline",
#         "jung": "connection, guidance, support, or a lifeline"
#     },
#     "lock": {
#         "freud": "secrets, repression, feeling confined, or a need for security",
#         "jung": "hidden potential, mystery, security, or something that needs to be opened"
#     },
#     "helmet": {
#         "freud": "protection of the mind, hidden thoughts, or a defensive posture",
#         "jung": "protection, defense of the ego, or intellectual safety"
#     },
#     "shield": {
#         "freud": "defense against threats, protection from reality, or emotional guarding",
#         "jung": "protection, defense against external influences, or inner strength"
#     },
#     "sword": {
#         "freud": "aggression, power, assertion, or cutting ties",
#         "jung": "truth, discrimination, justice, or spiritual power"
#     },
#     "throne": {
#         "freud": "desire for power, control, or superiority",
#         "jung": "authority, self-mastery, spiritual attainment, or wholeness"
#     },
#     "scepter": {
#         "freud": "authority, control, or a symbol of influence",
#         "jung": "power, spiritual authority, or the ability to lead"
#     },
#     "compass": {
#         "freud": "desire for direction, feeling lost, or a need for guidance",
#         "jung": "inner guidance, direction, moral alignment, or life's purpose"
#     },
#     "telescope": {
#         "freud": "desire to see further, curiosity, or an attempt to understand distant concepts",
#         "jung": "far-sightedness, understanding the larger picture, or spiritual vision"
#     },
#     "microscope": {
#         "freud": "attention to detail, anxiety over small things, or a need for scrutiny",
#         "jung": "introspection, understanding minute details, or insight into the hidden aspects of life"
#     },
#     "pen": {
#         "freud": "expression of thoughts, communication, or a desire for control",
#         "jung": "creativity, communication, conscious expression, or self-actualization"
#     },
#     "paper": {
#         "freud": "a blank slate, unexpressed thoughts, or a need for documentation",
#         "jung": "potential, conscious thought, memory, or the recording of one's journey"
#     },
#     "computer": {
#         "freud": "rational thought, control of information, or a desire for efficiency",
#         "jung": "logic, information processing, the conscious mind, or collective knowledge"
#     },
#     "television": {
#         "freud": "escapism, passive consumption of information, or external influence",
#         "jung": "collective consciousness, illusions, external reality, or the archetypal drama of life"
#     },
#     "photograph": {
#         "freud": "memory, attachment to the past, or a desire to preserve an image",
#         "jung": "memory, frozen moment in time, the past self, or the objective recording of inner states"
#     },
#     "table": {
#         "freud": "gathering, order, a place for interaction, or a foundation for thought",
#         "jung": "common ground, sharing, interaction, or the basis of a relationship"
#     },
#     "chair": {
#         "freud": "rest, stability, contemplation, or a desire for a defined position",
#         "jung": "rest, contemplation, authority (if empty), or inner peace"
#     },
#     "bed": {
#         "freud": "rest, unconscious state, comfort, or a place of vulnerability",
#         "jung": "restoration, unconscious realm, dreams, or intimacy (non-sexual context)"
#     },
#     "elevator": {
#         "freud": "rapid change, feeling of being controlled, or emotional shifts",
#         "jung": "quick ascent/descent through levels of consciousness, rapid change, or inner transformation"
#     },
#     "ladder": {
#         "freud": "ambition, ascent, vulnerability, or a path to higher status",
#         "jung": "spiritual ascent, progression through different levels of being, or conscious effort"
#     },
#     "wheel": {
#         "freud": "cycles, repetition, feeling trapped in routine, or a desire for movement",
#         "jung": "cycles of life, fate, wholeness, or dynamic movement"
#     },
#     "tunnel": {
#         "freud": "a passage, transition, feeling confined, or a journey through darkness",
#         "jung": "transition, a journey through the unconscious, a difficult passage leading to new light"
#     },
#     "lightbulb": {
#         "freud": "new idea, understanding, clarity, or an epiphany",
#         "jung": "consciousness, inspiration, sudden insight, or enlightenment"
#     },
#     "candle": {
#         "freud": "fragile hope, a limited light, or a focus for thought",
#         "jung": "individual consciousness, spiritual light, devotion, or inner wisdom"
#     },
#     "gear": {
#         "freud": "part of a system, feeling like a cog, or mechanical processes",
#         "jung": "interconnectedness, the mechanics of the psyche, or the necessity of precise function"
#     },
#     "maze": {
#         "freud": "confusion, feeling lost, internal conflicts, or a difficult challenge",
#         "jung": "the journey of individuation, self-discovery, or navigating complex inner conflicts"
#     },
#     "crossroads": {
#         "freud": "dilemma, choice, fear of making the wrong decision, or a turning point",
#         "jung": "a critical decision point, choice of life path, or spiritual crossroads"
#     },
#     "echo": {
#         "freud": "repetition of past experiences, unresolved issues, or a lingering memory",
#         "jung": "the reverberation of the collective unconscious, lingering influence, or a message from the past"
#     },
#     "silence": {
#         "freud": "repression, unspoken thoughts, fear of confrontation, or peace",
#         "jung": "introspection, profound peace, receptivity to inner wisdom, or the void before creation"
#     },
#     "dream": {
#         "freud": "manifestation of repressed desires, anxieties, or unconscious conflicts",
#         "jung": "messages from the unconscious, integration of the psyche, or a path to individuation"
#     },
#     "scream": {
#         "freud": "release of intense emotion, unexpressed trauma, or extreme fear",
#         "jung": "catharsis, intense emotional release, or a primal call for help"
#     },
#     "whisper": {
#         "freud": "hidden thoughts, secrets, subtle anxieties, or quiet communication",
#         "jung": "subtle messages from the unconscious, intuition, or a quiet revelation"
#     },
#     "laughter": {
#         "freud": "release of tension, defense mechanism, or joy masking underlying issues",
#         "jung": "release, joy, collective amusement, or spontaneous expression of the life force"
#     },
#     "hero": {
#         "freud": "ego ideal, a figure of strength or aspiration, or a projection of personal desires",
#         "jung": "the 'Hero' archetype, courage, overcoming obstacles, or the journey of self-discovery"
#     },
#     "fountain": {
#         "freud": "source of desires, emotional outpouring, or a childhood memory of abundance",
#         "jung": "source of life, renewal, spiritual energy, or inspiration"
#     },
#     "statue": {
#         "freud": "idealized self, rigid beliefs, or a symbol of unchangeable authority",
#         "jung": "archetypal form, enduring principle, frozen moment in time, or an aspect of the self made concrete"
#     },
#     "uniform": {
#         "freud": "conformity, repression of individuality, or a desire for belonging/authority",
#         "jung": "persona, social role, collective identity, or external conformity"
#     },
#     "coin": {
#         "freud": "value, worth, desire for material gain, or a small unit of exchange",
#         "jung": "self-worth or energy exchange"
#     },
#     "ticket": {
#         "freud": "desire for escape, access to new experiences, or permission to proceed",
#         "jung": "passage, entry into a new phase, opportunity, or authorization"
#     },
#     "bell": {
#         "freud": "warning, attention-seeking, or a signal of significant events",
#         "jung": "call to awareness, spiritual awakening, announcement, or a sacred sound"
#     },
#     "thunder": {
#         "freud": "anger, overwhelming emotion, sudden fear, or a powerful external force",
#         "jung": "divine power, sudden realization, spiritual awakening, or a profound emotional event"
#     },
#     "ice": {
#         "freud": "emotional coldness, repression of feelings, or stagnation",
#         "jung": "emotional detachment, rigidity, purification, or a dormant state"
#     },
#     "fog": {
#         "freud": "confusion, uncertainty, hidden elements, or a lack of clarity",
#         "jung": "mystery, the unknown, obscuring truth, or a state of unconsciousness"
#     },
#     "roots": {
#         "freud": "family origins, deep-seated issues, or primal grounding",
#         "jung": "foundation, ancestry, connection to the earth, or the source of life"
#     },
#     "seed": {
#         "freud": "unrealized potential, a hidden desire, or the beginning of growth",
#         "jung": "potential, new life, possibility, or the essence of something yet to unfold"
#     },
#     "shell": {
#         "freud": "protection, emotional barrier, or a fragile exterior",
#         "jung": "protection, boundaries, inner sanctuary, or the dwelling of the soul"
#     },
#     "labyrinth": {
#         "freud": "confusion, complex psychological conflicts, or a difficult path with no clear exit",
#         "jung": "the journey of individuation, a path of spiritual quest, or complex inner exploration"
#     },
#     "horizon": {
#         "freud": "future aspirations, limits of understanding, or the boundary of perception",
#         "jung": "the future, aspirations, the meeting point of conscious and unconscious, or new possibilities"
#     },
#     "globe": {
#         "freud": "control, worldly ambition, or feeling overwhelmed by vastness",
#         "jung": "wholeness, totality, the collective unconscious, or universal consciousness"
#     },
#     "scroll": {
#         "freud": "hidden knowledge, ancient wisdom, or a message from the past",
#         "jung": "ancient wisdom, sacred texts, destiny, or a unfolding life story"
#     },
#     "flute": {
#         "freud": "expression of delicate emotions, subtle desires, or a yearning for connection",
#         "jung": "harmony, inner voice, spiritual melody, or the expression of the soul"
#     },
#     "temple": {
#         "freud": "sacred desires, a place of personal reverence, or structured belief systems",
#         "jung": "sacred space within the self, spiritual center, collective wisdom, or a place of divine connection"
#     },
#     "web": {
#         "freud": "entrapment, complex relationships, or feeling ensnared by obligations",
#         "jung": "interconnectedness, creation, destiny, or intricate psychic patterns"
#     },
#     "abyss": {
#         "freud": "unconscious depths, overwhelming fear, or a sense of nothingness",
#         "jung": "the collective unconscious, void of creation, profound transformation, or facing the unknown"
#     },
#     "torch": {
#         "freud": "guidance, sudden insight, illumination of hidden thoughts, or a strong singular focus",
#         "jung": "light of consciousness, spiritual guidance, revelation, or inner truth"
#     },
#     "laurel wreath": {
#         "freud": "desire for recognition, achievement, honor, or past glories",
#         "jung": "victory, honor, spiritual triumph, or recognition of inner accomplishment"
#     },
#     "dust": {
#         "freud": "insignificance, decay, feeling overlooked, or the remnants of the past",
#         "jung": "mortality, ephemerality, return to origin, or the fundamental elements of existence"
#     },
#     "ash": {
#         "freud": "endings, loss, the residue of strong emotions (like anger), or purification through destruction",
#         "jung": "rebirth, renewal from destruction, memory of transformation, or the essence after a process"
#     },
#     "rust": {
#         "freud": "neglect, deterioration, stagnation, or a hidden process of decay",
#         "jung": "decay, neglect, time's passage, or the corrosive effects of inaction"
#     },
#     "mud": {
#         "freud": "primal state, messiness, feeling stuck, or emotional murkiness",
#         "jung": "primal matter, grounding, fertility, or the raw, unformed unconscious"
#     },
#     "sand": {
#         "freud": "transience, time slipping away, feeling unstable, or a vast, empty space",
#         "jung": "time, transformation, shifting foundations, or the vastness of unconscious elements"
#     },
#     "pillar": {
#         "freud": "support, strength, authority figures, or a rigid belief system",
#         "jung": "support, strength, steadfastness, cosmic axis, or a connection between heaven and earth"
#     },
#     "arch": {
#         "freud": "transition, a gateway to new experiences, or overcoming an obstacle",
#         "jung": "passage, transition, completion of a phase, or a threshold to the sacred"
#     },
#     "wings": {
#         "freud": "desire for escape, liberation, elevation, or a sense of lightness",
#         "jung": "transcendence, spiritual freedom, aspiration, or higher consciousness"
#     },
#     "cauldron": {
#         "freud": "a container for powerful emotions, a brewing of desires, or a transformative process",
#         "jung": "transformation, rebirth, healing, or the crucible of psychic integration"
#     },
#     "sponge": {
#         "freud": "absorption of emotions or experiences, a need for cleansing, or feeling drained",
#         "jung": "absorption, cleansing, receptivity, or the capacity to take in experiences"
#     },
#     "glove": {
#         "freud": "protection, concealment of one's true nature, or a desire for control over actions",
#         "jung": "persona, identity, protection from the world, or the conscious handling of a situation"
#     },
#     "net": {
#         "freud": "entrapment, complex relationships, or feeling ensnared by obligations",
#         "jung": "interconnectedness, destiny, collective unconscious (web-like), or something that catches knowledge/experience"
#     },
#     "feather": {
#         "freud": "lightness, fragility, a fleeting thought, or a desire for escape",
#         "jung": "spirit, freedom, transcendence, truth, or a connection to higher realms"
#     },
#     "hourglass": {
#         "freud": "anxiety about time, urgency, or the inevitable passage of life",
#         "jung": "time, mortality, balance, or the ongoing process of life and death"
#     },
#     "cradle": {
#         "freud": "early childhood memories, security, vulnerability, or a desire for nurturing",
#         "jung": "new beginnings, innocence, vulnerability, or the origin point of consciousness"
#     },
#     "tomb": {
#         "freud": "endings, finality, repressed memories buried, or fear of oblivion",
#         "jung": "a place of profound transformation, resting place of the old self, or a threshold to rebirth"
#     },
#     "roar": {
#         "freud": "unexpressed aggression, raw emotion, dominance, or a powerful internal urge",
#         "jung": "unleashed primal energy, assertion of power, instinctual expression, or a call to attention"
#     },
#     "cipher": {
#         "freud": "hidden messages, secrets, complex psychological mechanisms, or a desire for decoding",
#         "jung": "hidden knowledge, unconscious messages, the mysteries of the psyche, or a code of destiny"
#     },
#     "chalice": {
#         "freud": "a vessel for deep emotional needs, fulfillment, or receiving a significant offering",
#         "jung": "the Holy Grail, spiritual quest, container of wisdom, or sacred reception"
#     },
#     "anvil": {
#         "freud": "resistance, a place where character is forged through hardship, or a symbol of stubbornness",
#         "jung": "transformation, forging of character, destiny's workbench, or a place of creation through pressure"
#     },
#     "crucible": {
#         "freud": "intense emotional pressure, a test of resilience, or a process of painful purification",
#         "jung": "a place of intense transformation, purification, testing of the spirit, or alchemical process"
#     },
#     "magnifying glass": {
#         "freud": "desire for scrutiny, obsession with detail, or revealing hidden flaws",
#         "jung": "insight, deeper understanding, attention to detail, or uncovering hidden truths"
#     },
#     "blueprint": {
#         "freud": "a plan for life, unconscious design, or a desire for structure and control",
#         "jung": "the innate plan of the self, destiny's design, creative potential, or a map for individuation"
#     },
#     "crutches": {
#         "freud": "dependence, feeling vulnerable, a temporary support, or recovery from past injury",
#         "jung": "support during a difficult phase, temporary limitation, healing process, or reliance on external aid"
#     },
#     "scarecrow": {
#         "freud": "anxiety about protection, a false front, or feeling powerless despite outward appearance",
#         "jung": "protection (often illusory), persona, false appearance, or a warning against deception"
#     },
#     "sundial": {
#         "freud": "anxiety about time, seeking natural order, or a simple, unchanging measure",
#         "jung": "natural time, cosmic order, ancient wisdom, or cyclical processes"
#     },
#     "vine": {
#         "freud": "entanglement, growth that spreads uncontrollably, or a deep-rooted connection",
#         "jung": "growth, interconnectedness, resilience, or the flow of life energy"
#     },
#     "thorn": {
#         "freud": "pain, defense mechanism, hidden aggression, or a painful obstacle",
#         "jung": "protection, pain, sacrifice, or a challenge that causes growth"
#     },
#     "mushroom": {
#         "freud": "hidden dangers, sudden growth, or unconscious elements that emerge unexpectedly",
#         "jung": "growth from decay, hidden wisdom, spiritual insight, or ephemeral nature of life"
#     },
#     "crystal": {
#         "freud": "clarity, fragility, desire for purity, or a focus for energy",
#         "jung": "clarity, purity, healing, spiritual energy, or multifaceted truth"
#     },
#     "lightning": {
#         "freud": "sudden shock, intense emotional outburst, unexpected danger, or a flash of insight",
#         "jung": "divine intervention, sudden spiritual illumination, profound insight, or destructive creative energy"
#     },
#     "dew": {
#         "freud": "freshness, fleeting emotional states, or a subtle, quiet renewal",
#         "jung": "purity, spiritual refreshment, ephemeral beauty, or gentle blessings"
#     },
#     "canyon": {
#         "freud": "a deep emotional divide, a challenging passage, or a feeling of being overwhelmed by vastness",
#         "jung": "a profound journey inward, a test of endurance, sacred space, or a journey through the collective unconscious"
#     },
#     "oasis": {
#         "freud": "a place of temporary relief, escape from harsh reality, or a source of emotional sustenance",
#         "jung": "refuge, spiritual sustenance, hope in desolation, or a place of inner renewal"
#     },
#     "owl": {
#         "freud": "hidden fears, nocturnal activity, or quiet observation of one's surroundings",
#         "jung": "wisdom, intuition, insight into hidden truths, or the shadow self"
#     },
#     "fox": {
#         "freud": "cunning, deception, hidden desires, or adaptability in difficult situations",
#         "jung": "cunning, adaptability, trickster archetype, or intelligent navigation of challenges"
#     },
#     "raven": {
#         "freud": "ominous warnings, repressed anxieties about death, or a dark, wise figure",
#         "jung": "mystery, magic, prophecy, the shadow aspect of wisdom, or messenger of the unconscious"
#     },
#     "whale": {
#         "freud": "overwhelming emotions, vast unconscious drives, or a sense of being consumed by something greater",
#         "jung": "the collective unconscious, profound depth, ancient wisdom, or spiritual rebirth (being swallowed and emerging)"
#     },
#     "dolphin": {
#         "freud": "playfulness, desire for connection, or effortless movement through emotional waters",
#         "jung": "joy, playfulness, communication, spiritual guidance, or harmonious connection with the unconscious"
#     },
#     "coral": {
#         "freud": "complex structures, fragile dependencies, or a hidden, growing support system",
#         "jung": "community, interconnectedness, growth, beauty from organic processes, or the foundations of life"
#     },
#     "crying": {
#         "freud": "emotional release, unresolved grief, a plea for nurturing, or a regression to an earlier state",
#         "jung": "emotional catharsis, release of sorrow, purification, or a natural expression of inner pain"
#     },
#     "hunger": {
#         "freud": "primal need, unfulfilled desires, a yearning for gratification, or a feeling of emptiness",
#         "jung": "fundamental need, spiritual yearning, unfulfilled potential, or a driving force for growth"
#     },
#     "thirst": {
#         "freud": "a deep yearning, unfulfilled emotional needs, or a desperate search for relief",
#         "jung": "spiritual yearning, quest for truth/knowledge, or an essential need for fulfillment"
#     },
#     "illusion": {
#         "freud": "self-deception, avoidance of reality, or hidden desires that create false perceptions",
#         "jung": "maya (the veil of illusion), misperception of reality, or the need to see beyond surface appearances"
#     },
#     "mirage": {
#         "freud": "false hope, deception of the senses, or a desire for something unobtainable",
#         "jung": "illusion, false promise, spiritual longing, or the deceptive nature of the unconscious"
#     },
#     "eclipse": {
#         "freud": "temporary loss of conscious control, hidden aspects of personality, or a period of obscurity",
#         "jung": "temporary obscuring of consciousness, sacred alignment, hidden archetypal forces, or a phase of profound change"
#     },
#     "oath": {
#         "freud": "unconscious commitments, a binding promise, or a repressed sense of obligation",
#         "jung": "sacred commitment, unbreakable bond, self-imposed destiny, or integration of will"
#     },
#     "grace": {
#         "freud": "effortless movement, unearned favor, or a feeling of being guided by external forces",
#         "jung": "divine favor, spiritual blessing, effortless flow of life, or transcendent harmony"
#     },
#     "shovel": {
#         "freud": "digging into the past, uncovering repressed memories, burying emotions, or hard work",
#         "jung": "unearthing unconscious content, preparing new ground for growth, or burying the old self"
#     },
#     "pickaxe": {
#         "freud": "breaking through resistance, dismantling old patterns, or forcefully overcoming obstacles",
#         "jung": "breaking through psychological barriers, dismantling old structures, or initiating a new path"
#     },
#     "ramp": {
#         "freud": "gradual change, easing into a situation, or avoiding abrupt transitions",
#         "jung": "smooth transition, gradual ascent/descent in consciousness, or effortless progress"
#     },
#     "pocket": {
#         "freud": "hidden thoughts, personal resources, secrecy, or something kept close to oneself",
#         "jung": "hidden aspects of the self, untapped potential, or personal reserves"
#     },
#     "button": {
#         "freud": "a small point of control, a trigger for action, or a desire for connection/completion",
#         "jung": "a point of activation, decision, completion, or a fundamental connection"
#     },
#     "keyhole": {
#         "freud": "mystery, restricted access to information, a hidden path, or a desire to peer into the unknown",
#         "jung": "a glimpse into hidden realms, intuition, or a symbolic access point to the unconscious"
#     },
#     "latch": {
#         "freud": "temporary security, a barrier that can be easily opened, or a readiness for change",
#         "jung": "a light barrier, a threshold awaiting passage, or a symbolic closure/opening"
#     },
#     "cork": {
#         "freud": "suppression of emotions, containment of desires, or a temporary sealing off of something",
#         "jung": "containment, sealing off potential, or the suppression of vital energy"
#     },
#     "seal": {
#         "freud": "finality, authenticity, binding of a commitment, or marking ownership",
#         "jung": "completion, sacred promise, spiritual protection, or the stamp of destiny"
#     },
#     "ribbon": {
#         "freud": "connection, adornment, a binding force, or a decorative aspect of presentation",
#         "jung": "connection, celebration, beauty, or a symbolic bond"
#     },
#     "thread": {
#         "freud": "connection, the continuity of life, destiny, or the fragile link between things",
#         "jung": "the thread of life, destiny, interconnectedness, or the weaving of fate"
#     },
#     "needle": {
#         "freud": "precision, a piercing pain, the act of repair, or connecting disparate parts",
#         "jung": "precision, insight, healing, or the ability to mend what is broken"
#     },
#     "scissors": {
#         "freud": "separation, making a decisive break, division, or cutting ties with the past",
#         "jung": "discrimination, cutting away the unnecessary, making a choice, or severing old bonds"
#     },
#     "cobweb": {
#         "freud": "neglect, feeling trapped by stagnant situations, or old, fragile connections",
#         "jung": "stagnation, entrapment by past illusions, forgotten wisdom, or the delicate structures of time"
#     },
#     "cuffs": {
#         "freud": "restraint, feeling bound by circumstances, loss of personal freedom, or self-imposed limitations",
#         "jung": "limitation, self-imprisonment, a binding agreement (often subconscious), or a necessary restriction for growth"
#     },
#     "whistle": {
#         "freud": "a call for attention, a warning, simple communication, or a desire to be heard",
#         "jung": "a signal, intuition's call, a summons, or the awakening of consciousness"
#     },
#     "knapsack": {
#         "freud": "emotional burdens, preparation for a journey, personal resources carried, or self-reliance",
#         "jung": "the journey of the self, resources for individuation, burdens carried, or readiness for life's path"
#     },
#     "footprints": {
#         "freud": "the path taken, legacy, a trace of past actions, or following in someone else's steps",
#         "jung": "life's journey, the path of individuation, the indelible mark of existence, or following an archetypal pattern"
#     },
#     "cracks": {
#         "freud": "vulnerability, breaking points, hidden weaknesses, emotional fissures, or decay",
#         "jung": "opening for new insights, breaking of old forms, vulnerability leading to transformation, or a gateway to the unconscious"
#     },
#     "weed": {
#         "freud": "unwanted elements, resilience in adversity, disruption to order, or a persistent, nagging issue",
#         "jung": "wild growth, untamed nature, resilience, or a symbol of what needs to be acknowledged and integrated"
#     },
#     "burrow": {
#         "freud": "hiding from reality, seeking refuge, a secret passage, or a return to a primal, safe space",
#         "jung": "inner retreat, seeking security, exploration of the unconscious depths, or a place of incubation"
#     },
#     "cocoon": {
#         "freud": "a period of introversion, protection during a difficult phase, or waiting for an inevitable change",
#         "jung": "transformation, gestation of the new self, preparation for emergence, or a phase of profound inner work"
#     },
#     "fungus": {
#         "freud": "hidden decay, unseen proliferation, pervasive influence, or the decomposition of old ideas",
#         "jung": "decomposition of outdated forms, hidden growth, transformation of shadow material, or vital unseen processes"
#     },
#     "current": {
#         "freud": "unseen emotional forces, irresistible urges, feeling carried along by external influences",
#         "jung": "the flow of psychic energy, collective unconscious currents, destiny's movement, or an underlying spiritual force"
#     },
#     "quicksand": {
#         "freud": "feeling trapped, losing control, hidden dangers in a situation, or sinking into despair",
#         "jung": "a deceptive path, feeling overwhelmed by the unconscious, a test of grounding, or a dangerous spiritual trap"
#     },
#     "vapor": {
#         "freud": "elusiveness, fleeting thoughts, disappearing desires, or something lacking substance",
#         "jung": "formlessness, transience of material reality, spiritual essence, or the ephemeral nature of the psyche"
#     },
#     "gravity": {
#         "freud": "an irresistible pull, unavoidable consequences, feeling weighed down, or a grounding influence",
#         "jung": "fundamental law, destiny, inherent pull towards reality/grounding, or the weight of unconscious forces"
#     },
#     "disguise": {
#         "freud": "hiding one's true identity, assuming a false role, deception of self or others, or a defense mechanism",
#         "jung": "the persona, false self, concealment of the true self, or an act of symbolic transformation"
#     },
#     "interrogation": {
#         "freud": "confrontation of repressed truths, pressure to reveal secrets, or a self-examination under duress",
#         "jung": "a forced confrontation with the unconscious, seeking inner truth, or a process of self-discovery under pressure"
#     },
#     "vibration": {
#         "freud": "subtle energy, unseen emotional states, resonance with past experiences, or a barely perceptible tension",
#         "jung": "fundamental energy, resonance with archetypal patterns, subtle psychic communication, or the pulse of life force"
#     },
#     "acorn": {
#         "freud": "small beginnings leading to great potential, hidden growth, or the early stages of a desire",
#         "jung": "potential, growth, the seed of individuation, or the wisdom of nature's cycles"
#     },
#     "leaf": {
#         "freud": "growth, cycles of life and death, individuality (each unique), or shedding old attachments",
#         "jung": "life cycle, growth, connection to nature, or the ephemeral nature of existence"
#     },
#     "bark": {
#         "freud": "protection, outer defenses, resilience against external pressures, or hiding vulnerabilities",
#         "jung": "protection, inner strength, the skin of the soul, or the ancient wisdom of nature"
#     },
#     "sprout": {
#         "freud": "new beginnings, vulnerability of fresh desires, emerging potential, or a fragile hope",
#         "jung": "new beginnings, emerging consciousness, untapped potential, or the delicate start of individuation"
#     },
#     "hole": {
#         "freud": "emptiness, a void, a hidden opening, a perceived deficiency, or a way to escape",
#         "jung": "the unconscious, a passage, a space for new beginnings, or a psychological wound"
#     },
#     "spiral": {
#         "freud": "a repetitive pattern, a journey inward or outward, unconscious progression, or a cyclical nature of desires",
#         "jung": "individuation, growth, cosmic order, cyclical journey, or movement between conscious and unconscious"
#     },
#     "knot": {
#         "freud": "connection, entanglement in problems, feeling bound, or a point of tension",
#         "jung": "connection, psychological entanglement, a riddle, or a bond of fate"
#     },
#     "spindle": {
#         "freud": "the weaving of life's narrative, a central point of creation, or repetitive, monotonous activity",
#         "jung": "destiny, creation, the weaving of life's thread, or the axis of existence"
#     },
#     "ink": {
#         "freud": "expression of hidden thoughts, permanence of actions/words, a lasting mark, or a stain of guilt",
#         "jung": "conscious expression, permanence of truth, indelible impressions, or the fluid nature of creativity"
#     },
#     "paint": {
#         "freud": "transformation, expression of emotion, covering up reality, or artificiality",
#         "jung": "creativity, emotional expression, transformation of reality, or the projection of inner states"
#     },
#     "canvas": {
#         "freud": "a blank slate for new experiences, unexpressed potential, or a surface for projecting desires",
#         "jung": "potential, the self awaiting creation, the field of consciousness, or an opportunity for self-expression"
#     },
#     "brush": {
#         "freud": "precision in expression, applying a facade, or a tool for conscious creation",
#         "jung": "creative action, conscious will in shaping reality, or the instrument of transformation"
#     },
#     "chalk": {
#         "freud": "temporary marking, informal communication, fragility of plans, or childhood memories",
#         "jung": "temporary creation, impermanence, intuitive communication, or marking a sacred space"
#     },
#     "eraser": {
#         "freud": "correction of mistakes, desire to forget, removal of unpleasant memories, or second chances",
#         "jung": "redemption, forgiveness, removal of past errors, or the opportunity for a clean slate"
#     },
#     "vault": {
#         "freud": "security, containment of secrets, hidden desires, or fear of loss",
#         "jung": "inner sanctuary, repository of archetypal wisdom, containment of spiritual treasures, or guarded truths"
#     },
#     "chest": {
#         "freud": "hidden contents, personal memories, buried desires, or self-imposed burdens",
#         "jung": "repository of the self, personal history, hidden aspects of the psyche, or ancestral memories"
#     },
#     "diamond": {
#         "freud": "value, hardness, clarity of thought, or an unbreakable aspect of personality",
#         "jung": "wholeness, purity, spiritual light, invincibility, or ultimate truth"
#     },
#     "ruby": {
#         "freud": "passion, vitality, intense emotion, luxury, or a deep, sometimes hidden, desire",
#         "jung": "vitality, spiritual love, inner fire, or the concentrated energy of life"
#     },
#     "pearl": {
#         "freud": "hidden beauty, wisdom gained from adversity, purity, or an inner treasure cultivated",
#         "jung": "wisdom, inner treasure, purity gained through experience, or the perfected soul"
#     },
#     "gravel": {
#         "freud": "a rough path, small persistent difficulties, feeling unstable, or fragmented experiences",
#         "jung": "minor challenges, grounding, the fundamental elements of the journey, or a path of small steps"
#     },
#     "quill": {
#         "freud": "precise expression, old knowledge, delicate communication, or a desire for intellectual pursuit",
#         "jung": "wisdom, scholarly pursuit, conscious articulation of inner thoughts, or a connection to ancient knowledge"
#     },
#     "pendulum": {
#         "freud": "cycles of feeling, emotional oscillation, balance, or an external force controlling inner states",
#         "jung": "balance, rhythm of life, the interplay of opposites, or the movement between conscious and unconscious"
#     },
#     "scale": {
#         "freud": "balance of desires, justice, evaluation of self, or the weighing of choices/consequences",
#         "jung": "balance, justice, discernment, integration of opposites, or the process of objective self-assessment"
#     },
#     "hammer": {
#         "freud": "force, creation through effort, destruction of obstacles, or a tool for impact",
#         "jung": "creative power, focused will, transformation through forceful action, or the shaping of destiny"
#     },
#     "nail": {
#         "freud": "fixing something, piercing, a small but essential component, or a point of vulnerability",
#         "jung": "fixation, essential truth, security, or a point of connection/foundation"
#     },
#     "screw": {
#         "freud": "connection, twisting a situation, complexity, or a deeper, more secure binding",
#         "jung": "deeper connection, complex integration, persistent effort, or subtle influence"
#     },
#     "lever": {
#         "freud": "advantage, mechanical solution to a problem, or a simple way to achieve power",
#         "jung": "leverage for change, fundamental principle, finding the right point of action, or strategic insight"
#     },
#     "pulley": {
#         "freud": "assistance in overcoming difficulties, elevation, or being lifted by external forces",
#         "jung": "assistance from higher self/archetypes, overcoming resistance, or achieving elevation through cooperation"
#     },
#     "valve": {
#         "freud": "control of emotional flow, release of pressure, regulation of desires, or a blocked outlet",
#         "jung": "control of psychic energy, regulated expression, release of suppressed emotions, or a point of conscious choice"
#     },
#     "pipe": {
#         "freud": "conduit for desires/information, flow of emotional energy, connection between internal/external worlds",
#         "jung": "channel for psychic energy, conduit for transformation, connection between different levels of being, or a path of flow"
#     },
#     "cage": {
#         "freud": "feeling trapped, restraint of desires, self-imposed limitations, or fear of exposure",
#         "jung": "limitation, self-imprisonment, a protective but restrictive boundary, or a challenge to inner freedom"
#     },
#     "flame": {
#         "freud": "passion, focused energy, a flickering desire, or a subtle destructive potential",
#         "jung": "individual spirit, inner light, purification, or a spark of inspiration"
#     },
#     "echo chamber": {
#         "freud": "reinforcement of existing beliefs, avoidance of dissenting opinions, or a narcissistic psychological space",
#         "jung": "collective consciousness's influence, limited perspective, or the need to break free from repetitive thought patterns"
#     },
#     "gaze": {
#         "freud": "being observed, voyeurism, a desire for attention, or the critical eye of the superego",
#         "jung": "insight, perception, the inner eye, or confronting one's true self"
#     },
#     "threadbare": {
#         "freud": "wearing thin, approaching exhaustion, something losing its value, or neglected aspects of self",
#         "jung": "worn wisdom, vulnerability, the need for renewal, or a life lived to its fullest (for good or ill)"
#     },
#     "shroud": {
#         "freud": "concealment, hidden secrets, mourning, or avoidance of reality",
#         "jung": "mystery, hidden truth, transformation, or a transitional state"
#     },
#     "abacus": {
#         "freud": "rationalization, calculation of consequences, or a simple, logical approach to problems",
#         "jung": "order, calculation, logic, or a methodical approach to understanding the unconscious"
#     },
#     "parchment": {
#         "freud": "ancient knowledge, enduring truths, or a record of past experiences",
#         "jung": "ancient wisdom, historical record, spiritual teachings, or the enduring aspect of the soul"
#     },
#     "loom": {
#         "freud": "the weaving of life's narrative, control over destiny, or complex interdependencies",
#         "jung": "the weaving of fate, the creation of reality, the interconnectedness of psychic patterns, or the self's ongoing construction"
#     },
#     "incense": {
#         "freud": "appeasing higher powers, spiritual comfort, or a fleeting, sensory experience linked to memory",
#         "jung": "purification, spiritual atmosphere, prayer, or connection to the divine"
#     },
#     "amulet": {
#         "freud": "protection against anxiety, a source of perceived security, or a superstitious belief",
#         "jung": "protection, inner strength, connection to archetypal power, or a sacred object"
#     },
#     "talisman": {
#         "freud": "a personal charm for desires, focus for ambition, or belief in external power",
#         "jung": "magical power, inner transformation, manifestation of will, or a symbol of individuation"
#     },
#     "crest": {
#         "freud": "identity, family legacy, pride, or a symbol of social status",
#         "jung": "lineage, collective identity, personal totem, or the unique emblem of the self"
#     },
#     "mantle": {
#         "freud": "assuming a role, protection, hiding one's true self, or a burden of responsibility",
#         "jung": "authority, spiritual responsibility, inherited power, or a symbolic covering of the soul"
#     },
#     "cipher (tool)": {
#         "freud": "hiding communication, secret thoughts, or complex, indirect expressions",
#         "jung": "hidden language of the unconscious, intuitive understanding, or decoding spiritual messages"
#     },
#     "rune": {
#         "freud": "ancient wisdom, mysterious messages, or a primitive form of communication",
#         "jung": "esoteric knowledge, divine communication, archetypal symbols, or a key to destiny"
#     },
#     "pendulum (tool)": {
#         "freud": "a tool for prediction, a focus for neurotic obsessions, or seeking external answers",
#         "jung": "divination, unconscious guidance, rhythm of life, or a tool for psychic exploration"
#     },
#     "scale (tool)": {
#         "freud": "objective measurement, desire for fairness, or anxiety about comparison",
#         "jung": "justice, objectivity, balanced judgment, or the measurement of inner states"
#     },
#     "lever (tool)": {
#         "freud": "gaining advantage, exerting control, or a simple solution to a complex problem",
#         "jung": "finding the point of effective action, applying subtle force, or spiritual leverage"
#     },
#     "pulley (tool)": {
#         "freud": "assistance in overcoming burdens, external support, or mechanical advantage",
#         "jung": "facilitating progress, receiving support from higher forces, or spiritual aid"
#     },
#     "valve (tool)": {
#         "freud": "control of flow, emotional regulation, or a point of release/restriction",
#         "jung": "conscious control over psychic energy, regulated expression, release of suppressed emotions, or a point of intentional release"
#     },
#     "pipe (tool)": {
#         "freud": "channeling desires, controlled release of tension, or a conduit for gratification",
#         "jung": "channel for energy, spiritual connection, flow of information, or a passage for transformation"
#     },
#     "gavel": {
#         "freud": "authority, judgment, finality, or control over a situation",
#         "jung": "judgment, spiritual law, decisive action, or the voice of collective authority"
#     },
#     "hourglass (tool)": {
#         "freud": "measurement of time, anxiety about deadlines, or a reminder of fleeting pleasure",
#         "jung": "conscious awareness of time, mortality, the flow of life, or a meditation on impermanence"
#     },
#     "lantern": {
#         "freud": "limited insight, a small area of control, or cautious exploration of the unknown",
#         "jung": "individual consciousness, guidance through darkness, inner light, or a symbol of hope"
#     },
#     "mirror (tool)": {
#         "freud": "self-reflection, vanity, or a tool for observing external appearance",
#         "jung": "introspection, self-knowledge, the reflection of the unconscious, or a tool for seeing hidden truths"
#     },
#     "net (tool)": {
#         "freud": "capturing desires, feeling entangled, or a tool for control/acquisition",
#         "jung": "gathering knowledge, ensnaring illusions, interconnectedness, or the web of destiny"
#     },
#     "casket": {
#         "freud": "finality, burial of desires, hidden aspects of self, or the ending of a phase",
#         "jung": "completion, transformation, the container of the essential self, or a threshold to rebirth"
#     },
#     "compass (tool)": {
#         "freud": "seeking direction, control over one's path, or a reliance on external guidance",
#         "jung": "inner guidance, moral direction, alignment with purpose, or the tool for finding one's true north"
#     },
#     "telescope (tool)": {
#         "freud": "desire for distant observation, intellectual curiosity, or avoiding close-up reality",
#         "jung": "spiritual vision, cosmic perspective, expanding consciousness, or seeking universal truths"
#     },
#     "microscope (tool)": {
#         "freud": "intense scrutiny, obsession with detail, or revealing hidden flaws",
#         "jung": "introspection, understanding minute details, or insight into the hidden aspects of life"
#     },
#     "abacus (tool)": {
#         "freud": "rationalization, calculation of consequences, or a simple, logical approach to problems",
#         "jung": "order, calculation, logic, or a methodical approach to understanding the unconscious"
#     },
#     "sundial (tool)": {
#         "freud": "a natural measure of time, connection to primal rhythms, or a simple, unchanging measure",
#         "jung": "natural time, cosmic order, ancient wisdom, or cyclical processes"
#     },
#     "hourglass (tool)": {
#         "freud": "measurement of time, anxiety about deadlines, or a reminder of fleeting pleasure",
#         "jung": "conscious awareness of time, mortality, the flow of life, or a meditation on impermanence"
#     },
#     "gavel (tool)": {
#         "freud": "authority, judgment, finality, or control over a situation",
#         "jung": "judgment, spiritual law, decisive action, or the voice of collective authority"
#     },
#     "mantle (tool)": {
#         "freud": "assuming a role, protection, hiding one's true self, or a burden of responsibility",
#         "jung": "authority, spiritual responsibility, inherited power, or a symbolic covering of the soul"
#     },
#     "rune (tool)": {
#         "freud": "ancient wisdom, mysterious messages, or a primitive form of communication",
#         "jung": "esoteric knowledge, divine communication, archetypal symbols, or a key to destiny"
#     },
#     "flame (tool)": {
#         "freud": "passion, focused energy, a flickering desire, or a subtle destructive potential",
#         "jung": "individual spirit, inner light, purification, or a spark of inspiration"
#     },
#     "flock": {
#         "freud": "conformity, security in numbers, fear of standing out, or collective identity",
#         "jung": "collective consciousness, herd mentality, belonging, or the protective aspect of community"
#     },
#     "solstice": {
#         "freud": "a turning point, extremes of pleasure/pain, or the end of a cycle",
#         "jung": "cosmic rhythm, turning point in spiritual journey, balance of light and shadow, or a phase of transition"
#     },
#     "equinox": {
#         "freud": "balance between conflicting desires, equality, or a moment of psychological equilibrium",
#         "jung": "balance, harmony, equilibrium between opposites, or a point of transition between seasons of the soul"
#     },
#     "beacon": {
#         "freud": "guidance, a source of hope, or a warning of danger",
#         "jung": "spiritual guidance, hope, a calling, or a symbol of awakening consciousness"
#     },
#     "ruins": {
#         "freud": "decay, the remnants of the past, shattered dreams, or a feeling of loss and desolation",
#         "jung": "the remnants of the old self, forgotten wisdom, the impermanence of ego structures, or a site for rediscovery"
#     },
#     "gargoyle": {
#         "freud": "repressed fears, hidden aggression, grotesque aspects of the unconscious, or a protective but terrifying figure",
#         "jung": "the shadow archetype, guardian of the threshold, grotesque aspects of the psyche, or protection against evil"
#     },
#     "golem": {
#         "freud": "unthinking obedience, primitive power, a creation that turns against its maker, or uncontrolled urges",
#         "jung": "raw power, a creation of the ego that takes on its own life, elemental force, or the anima/animus in their primitive form"
#     },
#     "griffin": {
#         "freud": "dual nature, conflicting desires, power and control, or a symbol of strength and authority",
#         "jung": "balance of earthly and spiritual, integration of instincts, guardian of divine treasures, or a symbol of wisdom"
#     },
#     "dragon": {
#         "freud": "primal aggression, hidden destructive desires, formidable obstacles, or a symbol of overwhelming power",
#         "jung": "primal power, guardian of wisdom/treasure, confrontation with the unconscious, or inner transformation"
#     },
#     "phoenix": {
#         "freud": "rebirth from trauma, shedding old patterns, a cyclical return of energy, or a desire for self-renewal",
#         "jung": "rebirth, cyclical transformation, spiritual resurrection, or the transcendence of ego death"
#     },
#     "unicorn": {
#         "freud": "purity, elusive desires, a quest for innocence, or an unattainable ideal",
#         "jung": "purity, spiritual aspiration, healing, innocence, or the untamed spiritual self"
#     },
#     "chimera": {
#         "freud": "conflicting aspects of personality, impossible desires, fantastical creations, or fragmented self-identity",
#         "jung": "integration of disparate parts of the psyche, conflicting archetypes, or the struggle for wholeness"
#     },
#     "goblet": {
#         "freud": "a vessel for desires, gratification, or the consumption of intoxicating experiences",
#         "jung": "spiritual vessel, container for transformation, receiving divine grace, or the inner self's receptivity"
#     },
#     "saddle": {
#         "freud": "control over primal urges, readiness for a journey, or a burden being carried",
#         "jung": "control over the instinctual self (horse), preparation for journey, or readiness for individuation"
#     },
#     "bridle": {
#         "freud": "restraint of primal urges, discipline, or control over a powerful force",
#         "jung": "conscious control over instincts, self-discipline, or guiding one's path with intention"
#     },
#     "horse": {
#         "freud": "primal energy, untamed desires, strength, or a vehicle for unconscious drives",
#         "jung": "instinctual power, vital energy, inner freedom, or a vehicle for the spiritual journey"
#     },
#     "ox": {
#         "freud": "stubbornness, physical labor, plodding progress, or an unyielding force",
#         "jung": "strength, endurance, patient labor, or grounded, earthy power"
#     },
#     "ram": {
#         "freud": "aggression, stubbornness, forceful breakthrough, or a headstrong approach",
#         "jung": "leadership, determination, powerful breakthrough, or masculine principle"
#     },
#     "loom (textile machine)": {
#         "freud": "the mechanical process of creation, repetition, or the complex intertwining of elements",
#         "jung": "the weaving of destiny, creation of reality, the interconnectedness of psychic patterns, or the self's ongoing construction"
#     },
#     "crucible (vessel)": {
#         "freud": "a container for intense emotional reactions, a testing ground for desires, or a place of severe pressure",
#         "jung": "the alchemical vessel of transformation, a place of intense psychic pressure leading to integration, or purification"
#     },
#     "compass (directional instrument)": {
#         "freud": "a tool for direction, security in knowing one's path, or fear of being lost without external guidance",
#         "jung": "inner guidance, moral compass, finding one's true north, or the self's inherent direction"
#     },
#     "telescope (observational instrument)": {
#         "freud": "extending vision, intellectual curiosity, or distancing oneself from immediate problems by looking far away",
#         "jung": "expanding consciousness, cosmic perspective, seeing beyond immediate reality, or spiritual vision"
#     },
#     "microscope (observational instrument)": {
#         "freud": "intense scrutiny, obsession with detail, revealing hidden aspects, or anxiety about minute flaws",
#         "jung": "introspection, understanding minute details of the psyche, insight into hidden truths, or analytical precision"
#     },
#     "abacus (counting tool)": {
#         "freud": "calculation of consequences, methodical thinking, or a simple, predictable system for problem-solving",
#         "jung": "order, calculation, logic, or a methodical approach to understanding the unconscious"
#     },
#     "sundial (timekeeping tool)": {
#         "freud": "a natural measure of time, connection to primal rhythms, or a simple, unchanging measure",
#         "jung": "natural time, cosmic cycles, connection to archetypal timing, or a symbol of enduring wisdom"
#     },
#     "hourglass (timekeeping tool)": {
#         "freud": "the irreversible flow of time, anxiety about limitations, or a visual representation of life passing",
#         "jung": "conscious awareness of impermanence, transformation through time, balanced flow, or the soul's journey through time"
#     },
#     "gavel (ceremonial hammer)": {
#         "freud": "exerting authority, final judgment, or the decisive end to a conflict",
#         "jung": "conscious decision, spiritual law enacted, final judgment of the self, or a call to order in the psyche"
#     },
#     "mantle (garment/cloak)": {
#         "freud": "concealment of true identity, a protective layer, or the weight of responsibility assumed",
#         "jung": "persona, spiritual authority, inherited wisdom/power, or a symbolic covering of the soul"
#     },
#     "rune (alphabet/symbol)": {
#         "freud": "deciphering hidden meanings, personal symbols, or a connection to ancient, often repressed, knowledge",
#         "jung": "archetypal symbols, inner wisdom, messages from the collective unconscious, or a key to destiny"
#     },
#     "flame (visible part of fire)": {
#         "freud": "focused passion, a fragile but intense desire, or the controlled release of energy",
#         "jung": "individual spirit, inner light, purification, or a spark of inspiration"
#     },
#     "dawn": {
#         "freud": "new beginnings, hope after darkness, or the emergence of conscious desires",
#         "jung": "new consciousness, spiritual awakening, hope, or the birth of the self"
#     },
#     "twilight": {
#         "freud": "transition, ambiguity, the blending of conscious and unconscious, or a feeling of uncertainty",
#         "jung": "liminal space, transition between worlds, blurring of conscious/unconscious, or a time of introspection"
#     },
#     "foghorn": {
#         "freud": "a warning of hidden dangers, a call for help, or a sense of being lost in uncertainty",
#         "jung": "a call to awareness, a warning from the unconscious, or a guide through confusion"
#     },
#     "lighthouse": {
#         "freud": "guidance through difficult emotional waters, a stable point in chaos, or a watchful authority",
#         "jung": "guidance, hope, consciousness illuminating the unconscious, or a symbol of the self's enduring light"
#     },
#     "tide": {
#         "freud": "the rhythmic pull of unconscious forces, emotional ebb and flow, or uncontrollable natural cycles",
#         "jung": "cyclical nature of emotions, ebb and flow of psychic energy, or the unconscious's influence on life"
#     },
#     "reef": {
#         "freud": "hidden dangers, obstacles beneath the surface, or something that impedes progress",
#         "jung": "hidden obstacles, collective unconscious dangers, or a challenge to conscious navigation"
#     },
#     "current (oceanic)": {
#         "freud": "unseen forces influencing one's path, feeling carried along by desires, or a powerful underlying drive",
#         "jung": "the flow of life, collective unconscious currents, destiny's movement, or an underlying spiritual force"
#     },
#     "gale": {
#         "freud": "uncontrolled emotional outbursts, external pressures, or a violent disruption",
#         "jung": "powerful cleansing, spiritual force, major upheaval, or a cathartic release of energy"
#     },
#     "calm": {
#         "freud": "peace after conflict, repressed emotions, or a deceptive stillness before a storm",
#         "jung": "inner peace, tranquility, integration of opposites, or a state of spiritual equilibrium"
#     },
#     "whispering wind": {
#         "freud": "subtle anxieties, hidden messages, or an eerie, unsettling presence",
#         "jung": "subtle messages from the unconscious, intuitive insights, or the breath of spirit"
#     },
#     "petal": {
#         "freud": "fragility, beauty, delicate desires, or the outward expression of inner softness",
#         "jung": "delicacy, beauty, unfolding of the soul, or the ephemeral aspect of spiritual growth"
#     },
#     "thorn bush": {
#         "freud": "painful obstacles, self-protective mechanisms, or a defensive emotional barrier",
#         "jung": "challenges that protect deeper truths, necessary boundaries, or a test of resilience"
#     },
#     "root system": {
#         "freud": "deep-seated family issues, primal origins, or an extensive hidden support network",
#         "jung": "deep connection to collective unconscious, foundation of being, ancestral wisdom, or hidden nourishment"
#     },
#     "seed pod": {
#         "freud": "potential for growth, containment of future desires, or a protected inner world",
#         "jung": "potential, promise of new life, spiritual containment, or the vessel of future individuation"
#     },
#     "shell (crustacean)": {
#         "freud": "hard exterior protection, emotional armor, or a rigid defense mechanism",
#         "jung": "persona, protective covering, boundary of the ego, or a phase of necessary retreat"
#     },
#     "silt": {
#         "freud": "emotional residue, accumulated past experiences, or a muddying of clarity",
#         "jung": "accumulated psychic material, fertile ground for new growth (after cleansing), or unresolved unconscious elements"
#     },
#     "driftwood": {
#         "freud": "lost objects, feeling aimless, or the remnants of past journeys",
#         "jung": "resilience, what remains after a journey, found wisdom, or the unconscious bringing gifts from the depths"
#     },
#     "stone": {
#         "freud": "hardness, resistance to change, emotional rigidity, or a heavy burden",
#         "jung": "foundation, permanence, inner strength, or a symbol of the enduring self (lapis philosophorum)"
#     },
#     "pebble": {
#         "freud": "small irritations, minor obstacles, or something easily overlooked but present",
#         "jung": "small truths, minor challenges, or the foundational elements of growth"
#     },
#     "gemstone": {
#         "freud": "value, hidden beauty, inner purity, or a source of personal power/attraction",
#         "jung": "inner treasure, spiritual value, concentrated psychic energy, or a solidified aspect of the divine"
#     },
#     "quarry": {
#         "freud": "a source of raw materials, hard work, or digging into foundational aspects of self",
#         "jung": "a source of unconscious material, uncovering primal truths, or a place of significant inner excavation"
#     },
#     "gravel (path)": { # distinct from just "gravel" as material
#         "freud": "a difficult and uneven path, minor irritations on a journey, or progress that is slow but steady",
#         "jung": "a journey requiring attention, small steps of individuation, or a path of conscious effort"
#     },
#     "gorge": {
#         "freud": "a deep emotional divide, an overwhelming obstacle, or a profound separation",
#         "jung": "a deep passage into the unconscious, a place of initiation, or a profound natural barrier"
#     },
#     "passageway": {
#         "freud": "transition, a hidden route, or the journey between different psychological states",
#         "jung": "a threshold, a route to other realms of consciousness, or a journey of inner transformation"
#     },
#     "threshold": {
#         "freud": "a point of no return, a critical decision, or the boundary between inner and outer worlds",
#         "jung": "a sacred boundary, a point of initiation, a transition to a new level of consciousness, or the edge of the known"
#     },
#     "boundary": {
#         "freud": "limits, repression of desires, fear of stepping out of comfort zone, or self-imposed restrictions",
#         "jung": "ego limits, necessary differentiation, personal integrity, or the line between conscious and unconscious"
#     },
#     "barrier": {
#         "freud": "an obstacle, emotional defense, something blocking desires, or a feeling of entrapment",
#         "jung": "an obstacle to growth, a psychological defense, or a challenge to be overcome on the path of individuation"
#     },
#     "fortress": {
#         "freud": "strong ego defenses, emotional protection, isolation, or a desire for absolute security",
#         "jung": "the self's inner sanctuary, strong ego integration, protection of inner treasures, or a symbol of autonomy"
#     },
#     "outpost": {
#         "freud": "isolation, vigilance, a distant point of observation, or a precarious position",
#         "jung": "a point of conscious awareness in the unconscious, a place of vigilance, or exploring the outer limits of the self"
#     },
#     "citadel": {
#         "freud": "ultimate protection, impenetrable defenses, absolute control, or a powerful, unyielding ego",
#         "jung": "the core of the self, ultimate protection of inner wisdom, spiritual stronghold, or the integrated psyche"
#     },
#     "crypt": {
#         "freud": "hidden secrets, repressed memories, the unconscious mind, or a place of silent decay",
#         "jung": "a place of initiation, profound inner secrets, transformation through death and rebirth, or the wisdom of ancestors"
#     },
#     "coffin": {
#         "freud": "finality, fear of death, burying emotions, or the ending of a phase",
#         "jung": "transformation, symbolic death before rebirth, ending of an old self, or a container for what has passed"
#     },
#     "funeral": {
#         "freud": "grief, loss, dealing with endings, or the fear of being forgotten",
#         "jung": "ritual of transformation, letting go of the old, honoring cycles, or integrating loss into the self"
#     },
#     "mourning": {
#         "freud": "grief, unresolved loss, sadness, or a prolonged emotional state after an ending",
#         "jung": "a necessary psychological process of letting go, integration of loss, or a profound phase of inner work"
#     },
#     "weeping": {
#         "freud": "emotional release, catharsis of pain, a plea for sympathy, or unresolved trauma",
#         "jung": "purification through tears, release of psychic tension, deep emotional cleansing, or a connection to collective sorrow"
#     },
#     "sob": {
#         "freud": "intense emotional breakdown, uncontrollable grief, or a primal expression of helplessness",
#         "jung": "deep emotional release, catharsis, breakdown of ego defenses, or a profound reconnection with inner pain"
#     },
#     "giggle": {
#         "freud": "nervous release, suppressed amusement, or a light, often immature, expression of joy",
#         "jung": "innocent joy, spontaneous expression, the inner child at play, or a lighter aspect of the persona"
#     },
#     "chuckle": {
#         "freud": "contained amusement, a subtle expression of satisfaction, or a less overt release of tension",
#         "jung": "gentle amusement, inner satisfaction, a sign of contentment, or a benevolent aspect of the trickster"
#     },
#     "guffaw": {
#         "freud": "unrestrained amusement, a powerful release of energy, or a boisterous display of dominance",
#         "jung": "full-bodied release, authentic expression of joy, shared merriment, or a cathartic burst of energy"
#     },
#     "chasm": {
#         "freud": "a deep divide in the psyche, an insurmountable obstacle, or a profound emotional emptiness",
#         "jung": "a profound spiritual test, a gap between conscious and unconscious, or an unknown depth awaiting exploration"
#     },
#     "rift": {
#         "freud": "a split in personality, a growing division in relationships, or a crack in one's sense of reality",
#         "jung": "a division within the self, a breaking of old structures, or an opening for new insight"
#     },
#     "fissure": {
#         "freud": "a small but significant break, a hidden weakness, or the emergence of repressed issues",
#         "jung": "a subtle opening into the unconscious, a point of vulnerability, or a hint of underlying transformation"
#     },
#     "ledge": {
#         "freud": "a precarious position, a temporary resting place, or a narrow escape from danger",
#         "jung": "a transitional phase, a point of conscious observation, or a precarious but necessary foothold in inner journey"
#     },
#     "summit": {
#         "freud": "peak achievement, reaching a goal, or a feeling of being at the top of one's abilities",
#         "jung": "spiritual attainment, self-mastery, peak experience of individuation, or ultimate clarity"
#     },
#     "plateau": {
#         "freud": "a period of stagnation after progress, a stable but unmoving phase, or a feeling of limits reached",
#         "jung": "a period of integration, resting phase in development, or a time for consolidating gains before new growth"
#     },
#     "ridge": {
#         "freud": "a dividing line, a sharp transition, or a prominent feature in the psychological landscape",
#         "jung": "a dividing line in consciousness, a path of ascent/descent, or a significant landmark in the inner world"
#     },
#     "delta": {
#         "freud": "a branching out of desires, a spread of influence, or a point of dispersion after concentration",
#         "jung": "divergence of pathways, the distribution of psychic energy, or a fertile ground for new developments"
#     },
#     "estuary": {
#         "freud": "the merging of different emotional currents, a point of transition, or a mixture of influences",
#         "jung": "the merging of conscious and unconscious, a fertile spiritual ground, or a place of great energetic exchange"
#     },
#     "tributary": {
#         "freud": "a smaller influence feeding into a larger stream, a subsidiary desire, or a contributing factor",
#         "jung": "a contributing stream to the main life current, an influential inner force, or a source of psychic nourishment"
#     },
#     "watershed": {
#         "freud": "a critical turning point, a dividing line in emotional experiences, or a moment of significant impact",
#         "jung": "a critical point of transformation, a spiritual turning point, or a moment of profound insight that changes direction"
#     },
#     "maelstrom": {
#         "freud": "overwhelming emotional chaos, destructive urges, or a feeling of being pulled into a dangerous psychological vortex",
#         "jung": "a powerful transformative vortex, the destructive and creative force of the unconscious, or a necessary dissolution for rebirth"
#     },
#     "eddy": {
#         "freud": "repetitive thoughts, feeling stuck in a cycle, or a minor emotional disturbance",
#         "jung": "a cyclical psychic pattern, a contained emotional swirl, or a subtle current in the unconscious"
#     },
#     "undercurrent": {
#         "freud": "hidden desires, subtle influences, or unacknowledged emotional forces at play",
#         "jung": "unconscious influences, subtle spiritual currents, or a hidden driving force in the psyche"
#     },
#     "gust": {
#         "freud": "a sudden emotional impulse, a fleeting burst of energy, or an unexpected external influence",
#         "jung": "a sudden spiritual inspiration, a brief but powerful psychic impulse, or a moment of unexpected insight"
#     },
#     "breeze": {
#         "freud": "a light emotional touch, a subtle change, or a fleeting, gentle desire",
#         "jung": "gentle spiritual presence, subtle influence, or a moment of peaceful awareness"
#     },
#     "squall": {
#         "freud": "a brief but intense emotional outburst, a sudden conflict, or a passing difficulty",
#         "jung": "a sudden cleansing, a brief but intense spiritual challenge, or a quick release of tension"
#     },
#     "tempest": {
#         "freud": "a violent emotional storm, profound inner turmoil, or destructive psychological conflict",
#         "jung": "a powerful spiritual cleansing, profound inner upheaval leading to transformation, or a confrontation with primal forces"
#     },
#     "wither": {
#         "freud": "decay, loss of vitality, repressed emotional energy, or a feeling of being diminished",
#         "jung": "decline of the ego, necessary shedding of old forms, spiritual dryness before renewal, or the natural cycle of decay and rebirth"
#     },
#     "blossom": {
#         "freud": "unfolding desires, emergence of beauty, a fleeting moment of perfection, or the realization of potential",
#         "jung": "unfolding of the self, spiritual flowering, beauty of the soul, or the expression of divine potential"
#     },
#     "seedling": {
#         "freud": "vulnerable beginnings, nascent desires, fragile hopes, or the early stage of development",
#         "jung": "new beginnings, nascent consciousness, spiritual potential, or the delicate start of individuation"
#     },
#     "sapling": {
#         "freud": "young growth, developing strength, a flexible but growing aspect of self",
#         "jung": "developing strength, growing consciousness, flexible growth, or the emerging self"
#     },
#     "trunk": {
#         "freud": "core identity, stability, foundational strength, or the central part of a psychological structure",
#         "jung": "the axis of the self, foundational strength, connection between earthly and spiritual, or the core of consciousness"
#     },
#     "branch": {
#         "freud": "extensions of self, branching desires, connections to others, or new directions in life",
#         "jung": "diversification of the self, connections to the collective, new pathways of expression, or unfolding potential"
#     },
#     "foliage": {
#         "freud": "outward appearance, protective covering, lushness of desires, or a dense collection of thoughts",
#         "jung": "the vibrant expression of life, growth, hiding/revealing aspects of the self, or collective consciousness"
#     },
#     "canopy": {
#         "freud": "shelter from reality, a broad intellectual understanding, or an overarching protective structure",
#         "jung": "spiritual protection, a sheltering consciousness, encompassing wisdom, or the collective wisdom of the self"
#     },
#     "undergrowth": {
#         "freud": "hidden aspects, repressed desires, tangled emotional conflicts, or a chaotic inner state",
#         "jung": "the dense unconscious, primal instincts, unexplored psychic material, or hidden challenges"
#     },
#     "lichen": {
#         "freud": "slow, persistent growth, something overlooked but enduring, or a symbiotic relationship in the psyche",
#         "jung": "ancient wisdom, enduring life force, symbiotic relationships within the psyche, or resilience in harsh conditions"
#     },
#     "moss": {
#         "freud": "softness, quiet growth, decay, or a feeling of being covered/smothered by the past",
#         "jung": "ancient grounding, gentle growth, connection to the earth, or the soft embrace of the unconscious"
#     },
#     "fern": {
#         "freud": "ancient patterns, hidden growth, delicate structures, or a return to primal origins",
#         "jung": "ancient wisdom, hidden growth, symbolic of the spiral of life, or a connection to primordial consciousness"
#     },
#     "boulder": {
#         "freud": "a large, unmoving obstacle, stubborn resistance, or a heavy emotional burden",
#         "jung": "immovable truth, ancient wisdom, enduring presence, or a symbol of inner strength and stability"
#     },
#     "granite": {
#         "freud": "unyielding nature, absolute rigidity, unbreakable will, or a cold, unfeeling aspect of self",
#         "jung": "fundamental strength, enduring truth, resilience, or the unyielding core of the self"
#     },
#     "limestone": {
#         "freud": "accumulated layers of experience, a softer foundation, or something easily eroded over time",
#         "jung": "transformation through time, accumulated wisdom, porous nature of the psyche, or foundational material of consciousness"
#     },
#     "obsidian": {
#         "freud": "sharp insights, hidden dangers, a protective but brittle exterior, or the unconscious's darker aspects",
#         "jung": "deep introspection, shadow work, truth that cuts, or a protective but unyielding spiritual mirror"
#     },
#     "slate": {
#         "freud": "a blank surface for recording, easily broken memories, or a simple, utilitarian purpose",
#         "jung": "a surface for karmic imprints, a record of the soul's journey, or a simple, profound truth"
#     },
#     "geode": {
#         "freud": "a rough exterior hiding inner beauty, unexpected revelations, or a surprising depth of feeling",
#         "jung": "hidden spiritual beauty, discovery of inner wisdom, unexpected treasures within the self, or profound inner transformation"
#     },
#     "fossil": {
#         "freud": "ancient memories, repressed past, enduring impact of trauma, or something preserved from a bygone era",
#         "jung": "ancestral wisdom, collective unconscious memories, a remnant of primordial life, or a solidified archetype"
#     },
#     "amber": {
#         "freud": "preservation of memory, something trapped in time, warmth, or a comforting presence from the past",
#         "jung": "ancient wisdom, preserved life force, healing, or a solidified form of spiritual energy"
#     },
#     "resin": {
#         "freud": "a sticky situation, something that binds, or a natural defense mechanism",
#         "jung": "healing, purification, natural protection, or the essence of life's resilience"
#     },
#     "beach": {
#         "freud": "a place of escape, relaxation, or where conscious thoughts meet underlying emotional currents; can symbolize a desire for uninhibited freedom or a return to simpler states of mind.",
#         "jung": "a liminal space representing the boundary between the conscious (land) and the unconscious (sea); a place of integration, transition, or where unconscious material emerges into awareness, suggesting renewal and self-discovery."
#     },
#     "ghost": {
#         "freud": "unresolved past issues, repressed memories, guilt, or fear of the unknown",
#         "jung": "ancestral spirits, unintegrated aspects of the psyche, the shadow, or a connection to the collective unconscious"
#     },
#     "graveyard": {
#         "freud": "fear of death, loss, suppressed grief, or the end of a life phase",
#         "jung": "place of transformation, ancestral wisdom, confronting mortality, or the resting place of old selves"
#     },
#     "skeleton": {
#         "freud": "fear of decay, the core truth exposed, or the fundamental structure beneath the surface",
#         "jung": "mortality, fundamental truth, structure of being, or the essence that remains after illusion"
#     },
#     "coffin": {
#         "freud": "fear of confinement, endings, repression of life, or a desire for oblivion",
#         "jung": "containment of the old self, transition, initiation into new life, or a period of dormancy before rebirth"
#     },
#     "haunted house": {
#         "freud": "the self as troubled by past traumas, unresolved family dynamics, or repressed psychological complexes",
#         "jung": "the psyche containing unintegrated complexes, ancestral patterns, or a need to confront buried aspects of self"
#     },
#     "monster": {
#         "freud": "repressed fears, destructive urges, projections of inner conflicts, or overwhelming anxieties",
#         "jung": "the shadow, primal instincts, the destructive aspect of an archetype, or unintegrated psychic content"
#     },
#     "chainsaw": {
#         "freud": "aggressive impulses, destructive power, cutting ties, or overwhelming force",
#         "jung": "raw power, force of nature, decisive action, or a tool for radical transformation/clearing"
#     },
#     "doll": {
#         "freud": "childhood innocence lost, feeling controlled, or a representation of an idealized/traumatized self",
#         "jung": "the inner child, persona, archetypal human form, or a vessel for projection"
#     },
#     "spiderweb": {
#         "freud": "entrapment, feeling caught in a sticky situation, or intricate anxieties",
#         "jung": "interconnectedness, creation, destiny, or the intricate patterns of the unconscious"
#     },
#     "curse": {
#         "freud": "feeling burdened by past events, guilt, or the perceived malevolence of others/fate",
#         "jung": "a psychological complex, inherited collective pattern, or the consequences of unacknowledged actions"
#     },
#     # Spiritual-themed symbols
#     "aura": {
#         "freud": "unconscious emanation of one's emotional state, a subtle manifestation of desire or anxiety",
#         "jung": "the energetic field of the self, a visible manifestation of the soul or individuation, or a psychic emanation"
#     },
#     "chakra": {
#         "freud": "points of psychological energy related to specific desires or anxieties in the body",
#         "jung": "centers of spiritual energy, stages of consciousness, or focal points for psychic integration"
#     },
#     "mandala": {
#         "freud": "a personal attempt to organize chaotic thoughts, or a symbolic representation of the self's desired perfection",
#         "jung": "the archetype of the self, wholeness, psychic order, or the journey of individuation"
#     },
#     "meditation": {
#         "freud": "a retreat from reality to manage anxiety, or a focus on internal sensations/thoughts",
#         "jung": "a path to the unconscious, self-discovery, spiritual grounding, or integration of inner and outer worlds"
#     },
#     "altar": {
#         "freud": "a place for suppressed desires or anxieties to be 'sacrificed' or brought into focus, a symbol of devotion to an internal ideal",
#         "jung": "a sacred space for inner offerings, connection to the divine, integration of the spiritual and material, or devotion to the self's higher purpose"
#     },
#     "ritual": {
#         "freud": "a repetitive action to manage anxiety, a symbolic acting out of unconscious desires or conflicts",
#         "jung": "a symbolic act to connect with the archetypes, a way to structure psychic energy, or a process of transformation"
#     },
#     "oracle": {
#         "freud": "a projection of one's own unconscious knowledge or anxieties, or a desire for external guidance",
#         "jung": "a source of collective wisdom, intuition, a messenger from the unconscious, or a guide on the path of individuation"
#     },
#     "zenith": {
#         "freud": "the peak of ambition, a moment of triumph over internal conflict, or a temporary escape from earthly desires",
#         "jung": "the highest point of spiritual attainment, conscious awareness, self-realization, or a moment of clarity"
#     },
#     "cosmic egg": {
#         "freud": "the primal state of being, unformed desires, or the potential for new psychological development",
#         "jung": "the totality of existence, primordial potential, the universe as a unified whole, or the source of all archetypes"
#     },
#     "divine spark": {
#         "freud": "an inherent potential for creativity or powerful, repressed instincts, a drive towards self-preservation or expression",
#         "jung": "the uncreated self, innate spiritual potential, a connection to the numinous, or the essence of the Self within"
#     },
#     "vampire": {
#         "freud": "parasitic relationships, repressed destructive urges, fear of control/domination, or unresolved anxieties about vitality",
#         "jung": "the shadow archetype, consuming aspects of the psyche, psychic drain, or the immortal/eternal aspect of the unconscious"
#     },
#     "werewolf": {
#         "freud": "uncontrolled primal instincts, aggression, suppressed rage, or fear of one's own 'animalistic' nature",
#         "jung": "the wild or untamed shadow, instinctual power, a regression to primitive states, or the integration of human and animal nature"
#     },
#     "zombie": {
#         "freud": "feeling emotionally dead or without agency, overwhelming anxiety about external threats, or repressed fear of conformity",
#         "jung": "the collective unconscious acting without individual consciousness, a loss of soul, mindless conformity, or unintegrated instinctual drives"
#     },
#     "mummy": {
#         "freud": "feeling trapped by the past, unresolved issues from ancestry, or fear of stagnation and decay",
#         "jung": "the past, ancient wisdom trapped or awaiting release, the immortal aspect of the self, or a connection to collective memory"
#     },
#     "witch": {
#         "freud": "feared female authority figures, projections of manipulative intent, or repressed desires for power/control",
#         "jung": "the wise old woman archetype (positive or negative), primal feminine power, intuition, or the shadow aspect of creativity"
#     },
#     "cult": {
#         "freud": "desire for belonging and acceptance, fear of individuality, or submission to an overwhelming authority figure",
#         "jung": "collective neurosis, unconscious group dynamics, the shadow side of spiritual seeking, or the loss of individual consciousness within a collective"
#     },
#     "asylum": {
#         "freud": "mental instability, feeling trapped by one's own mind, repressed irrational thoughts, or fear of losing control",
#         "jung": "the inner chaos of the psyche, a place for confronting madness or fragmented aspects of self, or the need for psychological healing"
#     },
#     "chains": {
#         "freud": "feeling bound by obligations, repressed desires, or inner conflicts, fear of helplessness",
#         "jung": "limitations, unacknowledged complexes, self-imposed restrictions, or the need for liberation and spiritual freedom"
#     },
#     "fog (thick)": {
#         "freud": "confusion, obscured thoughts, inability to see clearly into situations, or suppressed anxieties creating mental murkiness",
#         "jung": "the unconscious, mystery, the unknown, a veil over truth, or a state of not-knowing that precedes new insight"
#     },
#     "screaming (unheard)": {
#         "freud": "repressed trauma, unexpressed anger or pain, feeling unheard or ignored, or an internal cry for help",
#         "jung": "a powerful but unacknowledged cry from the unconscious, a sign of inner torment that needs to be integrated, or a collective unheard plea"
#     },
#     "decay/rot": {
#         "freud": "fear of deterioration, loss of vitality, unresolved past experiences, or the unpleasant truth of endings",
#         "jung": "transformation, the cycle of death and rebirth, dissolution of old forms, or the natural process of decomposition leading to new life"
#     },
#     "eyes (watching)": {
#         "freud": "fear of judgment, paranoia, feeling exposed, or the internal gaze of the superego",
#         "jung": "consciousness, divine presence, universal awareness, or the watchful archetypal Self"
#     },
#     "whispers (unintelligible)": {
#         "freud": "subliminal anxieties, secrets, or the nagging voice of guilt/repressed thoughts",
#         "jung": "unconscious communications, subtle intuitions, messages from the collective unconscious, or hints of hidden knowledge"
#     },
#     "silence (ominous)": {
#         "freud": "repression, unspoken truths, anticipation of conflict, or the quiet before a mental breakdown",
#         "jung": "the quiet of the unconscious, a moment before revelation, the suspension of conscious activity, or the profound stillness of the Self"
#     },
#     "grave": {
#         "freud": "finality, loss, fear of being forgotten, or a place where repressed memories are buried",
#         "jung": "transition, a resting place for the old ego, a gateway to rebirth, or a symbol of deep introspection"
#     },
#     "labyrinth (endless)": {
#         "freud": "feeling lost, overwhelming psychological complexities, an inescapable mental trap, or unresolved inner conflicts",
#         "jung": "the journey of individuation, a complex psychic process, a descent into the unconscious, or a path of self-discovery without a clear end"
#     },
#     "shadow figure": {
#         "freud": "projections of one's own negative traits, suppressed urges, or a manifestation of internalized fear",
#         "jung": "the unintegrated shadow self, an autonomous complex, or a manifestation of the collective shadow"
#     },
#     "old photo (distorted)": {
#         "freud": "distorted memories, trauma from the past, an uncomfortable truth about one's history, or the decay of remembrance",
#         "jung": "a warped or partial view of the past, the subjective nature of memory, or a glimpse into ancestral patterns distorted by time"
#     },
#     "creeping vines": {
#         "freud": "feeling entangled by relationships or circumstances, invasive thoughts, or a slow but pervasive sense of decay",
#         "jung": "nature's reclaiming, slow growth, interconnectedness that can also bind, or the subtle but persistent influence of the unconscious"
#     },
#     "rotting wood": {
#         "freud": "decay of foundations, a crumbling sense of security, neglect, or the inevitable deterioration of something once strong",
#         "jung": "the natural cycle of decomposition, the breakdown of old structures to allow for new growth, or the need to release what is no longer viable"
#     },

# "lotus flower": {
#         "freud": "purity amidst desires, emotional unfolding, or spiritual aspiration overcoming materialistic urges",
#         "jung": "spiritual purity, rebirth, growth from darkness into light, enlightenment, or the unfolding of the Self"
#     },
#     "om symbol": {
#         "freud": "a focus for internal resonance, a desire for mental stillness, or a connection to primal sounds",
#         "jung": "the primordial sound of creation, cosmic vibration, unity of all existence, or the essence of divine presence"
#     },
#     "ankh": {
#         "freud": "desire for longevity, a primal connection to vitality, or the unresolved fear of death",
#         "jung": "life, immortality, spiritual power, or the union of opposing forces (masculine and feminine principles for life's creation)"
#     },
#     "hamsa hand": {
#         "freud": "a desire for protection from anxiety or fear, a projection of security, or a need for external validation",
#         "jung": "divine protection, blessings, good fortune, or the presence of the spiritual world"
#     },
#     "yin and yang": {
#         "freud": "the balance of opposing internal forces, the integration of desires and repressions, or the harmony of internal conflicts",
#         "jung": "the balance and interconnectedness of opposites (light/dark, masculine/feminine) within the psyche, wholeness, or integration"
#     },
#     "tree of life": {
#         "freud": "family roots, the growth of the self, connection to a larger lineage, or the source of personal vitality",
#         "jung": "connection between heaven and earth, spiritual growth, universal interconnectedness, wisdom, or the archetype of the Self"
#     },
#     "phoenix": {
#         "freud": "resilience in the face of loss, the ability to overcome past traumas, or a desire for radical transformation",
#         "jung": "rebirth, renewal from destruction, resurrection, triumph over adversity, or eternal life"
#     },
#     "infinity symbol": {
#         "freud": "a desire for unending pleasure or control, a denial of limits, or a projection of eternal existence",
#         "jung": "eternity, boundless potential, continuous flow, or the interconnectedness of all things"
#     },
#     "chakras (individual)": {
#         "freud": "specific bodily locations where emotional energy or anxieties are felt, related to particular desires or repressed instincts",
#         "jung": "individual energy centers, representing specific aspects of consciousness and spiritual development, or the integration of mind-body-spirit"
#     },
#     "sacred geometry": {
#         "freud": "an attempt to find order in chaos, a desire for structure, or the intellectual pursuit of underlying patterns",
#         "jung": "the blueprint of creation, universal order, the underlying structure of the psyche, or the interconnectedness of all forms"
#     },
#     "holy well": {
#         "freud": "a source of hidden desires, a place for emotional cleansing, or a return to primal origins",
#         "jung": "a source of spiritual healing, divine wisdom, renewal, or a gateway to the collective unconscious"
#     },
#     "shrine": {
#         "freud": "a place of personal devotion, a focus for idealized desires, or a sanctuary for repressed thoughts",
#         "jung": "a sacred space within the self, a place of reverence, connection to higher ideals, or an altar for personal spiritual practice"
#     },
#     "pilgrimage": {
#         "freud": "a journey to resolve inner conflicts, a search for external validation, or an escape from daily anxieties",
#         "jung": "a spiritual journey, a quest for inner truth, a movement towards individuation, or a path of self-discovery"
#     },
#     "incense": {
#         "freud": "a sensory experience tied to past memories or emotional states, a calming agent for anxiety, or a subtle release of suppressed desires",
#         "jung": "purification, spiritual atmosphere, offering to the divine, or the elevation of consciousness"
#     },
#     "drum": {
#         "freud": "primal rhythms, a release of contained energy, or a call to attention",
#         "jung": "the heartbeat of the universe, rhythmic connection to the earth, sacred sound, or a call to altered states of consciousness"
#     },
#     "chanting": {
#         "freud": "repetitive vocalization for stress relief, a release of emotional tension, or a way to focus the mind on a specific desire",
#         "jung": "sacred sound, connection to the collective, meditative practice, or the resonance of archetypal energies"
#     },
#     "altar cloth": {
#         "freud": "a symbolic covering for hidden desires, a desire for purity in ritual, or a visual representation of sacred space",
#         "jung": "purity, sanctity, preparation for sacred work, or a symbolic boundary for spiritual practice"
#     },
#     "rosary/prayer beads": {
#         "freud": "repetitive action to alleviate anxiety, a focus for suppressed desires, or a tangible connection to a belief system",
#         "jung": "meditative aid, counting prayers, connection to the divine, or a tool for centering the self"
#     },
#     "holy text": {
#         "freud": "source of authority, a guide for moral conduct (superego), or a focus for intellectual desires",
#         "jung": "sacred wisdom, collective knowledge, guidance for the spiritual journey, or archetypal narratives"
#     },
#     "meditation cushion": {
#         "freud": "a physical support for mental stillness, a place for introspection, or a symbol of withdrawal from external stimuli",
#         "jung": "a place for grounding, support for inner work, centering the self, or a space for spiritual discipline"
#     },
#     "sacred smoke": {
#         "freud": "a release of tension, a connection to primal cleansing, or a symbolic dissipation of anxieties",
#         "jung": "purification, offering to the spirits, transformation, or a connection to the unseen realms"
#     },
#     "prayer flag": {
#         "freud": "a visible manifestation of desires, a hope for external intervention, or a symbolic release of intentions",
#         "jung": "intention, blessing, energetic offering, or a connection between human aspiration and cosmic energy"
#     },
#     "gong": {
#         "freud": "a sudden, powerful sound that startles or focuses the mind, a release of accumulated tension",
#         "jung": "sacred sound, energetic clearing, call to mindfulness, or a vibration that resonates with the collective unconscious"
#     },
#     "amulet/talisman": {
#         "freud": "a source of perceived external power, a way to manage anxiety through superstition, or a projection of personal desires for protection",
#         "jung": "protection, personal power, connection to archetypal forces, or a tangible symbol of inner strength and belief"
#     },
#     "spiritual guide (animal or human)": {
#         "freud": "a projection of an idealized self or authority figure, a desire for mentorship, or a manifestation of the superego's influence",
#         "jung": "an archetype of wisdom, a messenger from the unconscious, a helping spirit, or a representation of the Self's guidance"
#     },
#     "sacred mountain": {
#         "freud": "an ultimate challenge, a lofty aspiration, or a place of escape from earthly concerns",
#         "jung": "a place of spiritual ascent, transcendence, connection to the divine, or the peak of individuation"
#     },
#     "stupa/pagoda": {
#         "freud": "a structured representation of belief, a desire for spiritual order, or a symbol of containment for sacred ideas",
#         "jung": "a cosmic diagram, a sacred dwelling, a place of spiritual pilgrimage, or a symbol of enlightenment and the collective unconscious"
#     },
#     "holy grail": {
#         "freud": "the ultimate desire, an unattainable goal, or the object of a lifelong search for fulfillment",
#         "jung": "the ultimate spiritual quest, wholeness, self-realization, or the source of divine sustenance"
#     },
#     "celestial bodies (specific planets/stars)": {
#         "freud": "external influences on personal fate, aspirations towards greatness, or a connection to universal patterns beyond control",
#         "jung": "archetypal influences, cosmic patterns, destiny, or connection to the universal forces that shape the individual psyche"
#     },
#     "the void": {
#         "freud": "fear of nothingness, anxiety of emptiness, or the absence of structure/desire",
#         "jung": "the fertile ground of creation, the source of all potential, profound stillness, or the pre-conscious state from which new ideas emerge"
#     }
# }

# # def extract_symbols(text):
# #     doc = nlp(text.lower())
# #     keywords = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'PROPN', 'VERB', 'ADJ','ADV']]
# #     normalized_dict = {k.lower(): v for k, v in symbol_dict.items()}
# #     matched_symbols = {k: normalized_dict[k] for k in normalized_dict if k in keywords}

# #     return matched_symbols


# # def detect_emotion(text):
# #     analysis = TextBlob(text)
# #     polarity = analysis.sentiment.polarity
# #     if polarity > 0.3:
# #         return "positive"
# #     elif polarity < -0.3:
# #         return "negative"
# #     else:
# #         return "neutral"

# # def interpret_dream(text):
# #     symbols = extract_symbols(text)
# #     emotion = detect_emotion(text)
# #     interpretation = []

# #     if symbols:
# #         interpretation.append("🌀 Symbolic Interpretations:")
# #         for symbol, theories in symbols.items():
# #             interpretation.append(f"- {symbol}:")
# #             for theory, meaning in theories.items():
# #                 interpretation.append(f"  - _{theory.capitalize()}_: {meaning}")
# #     else:
# #         interpretation.append(" No symbolic matches found in this dream.")

# #     interpretation.append(f"\n Overall Emotional Tone: _{emotion}_")
    
# #     return "\n".join(interpretation), list(symbols.keys()), emotion
# def extract_symbols(text):
#     doc = nlp(text.lower())
    
#     # Collect both raw tokens and lemmas for flexible matching
#     tokens = set()
#     for token in doc:
#         if token.pos_ in ['NOUN', 'PROPN', 'VERB', 'ADJ', 'ADV']:
#             tokens.add(token.text.lower())
#             tokens.add(token.lemma_.lower())
    
#     # Match any symbol in the dict that appears in the token set
#     normalized_dict = {k.lower(): v for k, v in symbol_dict.items()}
#     matched_symbols = {k: v for k, v in normalized_dict.items() if k in tokens}
    
#     return matched_symbols


# def detect_emotion(text):
#     analysis = TextBlob(text)
#     polarity = analysis.sentiment.polarity
#     if polarity > 0.3:
#         return "positive"
#     elif polarity < -0.3:
#         return "negative"
#     else:
#         return "neutral"


# def interpret_dream(text):
#     symbols = extract_symbols(text)
#     emotion = detect_emotion(text)
#     interpretation = []

#     if symbols:
#         interpretation.append("🌀 Symbolic Interpretations:")
#         for symbol, theories in symbols.items():
#             interpretation.append(f"{symbol}:")
#             for theory, meaning in theories.items():
#                 interpretation.append(f"{theory.capitalize()}: {meaning}")
#     else:
#         interpretation.append(" No symbolic matches found in this dream.")

#     interpretation.append(f"\n Overall Emotional Tone: {emotion}")
    
#     return "\n".join(interpretation), list(symbols.keys()), emotion
from gemini_module import interpret_dream_with_gemini

def interpret_dream(dream_text):
    interpretation = interpret_dream_with_gemini(dream_text)

    # Optional placeholders or enhancements
    symbols = []  # Add symbol extraction if needed
    emotion = "mystical"  # Placeholder or analyze based on response

    return interpretation, symbols, emotion
