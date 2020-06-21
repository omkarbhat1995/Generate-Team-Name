#!/usr/bin/env python3
# constants
verb = ["Team"]
noun = ["Association", "Band", "Body", "Bunch", "Class", "Cohort", "Company", "Crowd", "Gang", "Group", "Lot", "Mass",
        "Party", "Posse", "Set", "Society", "Squad", "Staff", "Team", "Tribe", "Group", "Crowd", "Gang", "Squad",
        "Faculty", "Colony", "onlookers", "Audience", "Jury", "Team", "Army", "Troupe","Company", "Corporation"]
adj_neg = ['Disciplined', 'Dark', 'Exceptional', 'Quick-Witted', 'Fair', 'Creative', 'Concerned', 'Conscientious',
       'Cautious', 'Formal', 'Helpful', 'Obliging', 'Individualistic', 'Discerning', 'Truthful', 'Enchanting',
       'Fantastic', 'Diligent', 'Dependable', 'Short', 'Able', 'Reasonable', 'Laid-Back', 'Secure', 'Authentic',
       'Leader', 'Fine', 'Fabulous', 'Pretty', 'Sane', 'Caring', 'Perceptive', 'Jolly', 'Intellectual', 'Curious',
       'Wonderful', 'Free', 'Fool', 'Entertaining', 'Polite', 'Eminent', 'Pleasing', 'Gutsy', 'Tidy', 'Hopeful',
       'Receptive', 'Quiet', 'Forgiving', 'Vivacious', 'Light-Hearted', 'Wise', 'Private', 'Versatile', 'Warmhearted',
       'Perfect', 'Distinct', 'Loving', 'Gentle', 'Passionate', 'Competent', 'Contrary', 'Genuine', 'Inventive',
       'Convivial', 'Great', 'Artistic', 'Self-Controlled', 'Humble', 'Affable', 'Joyous', 'Proud', 'Vigilant',
       'Motivated', 'Persevering', 'Purposeful', 'Feisty', 'Rambling', 'Sad', 'Delightful', 'Realistic',
       'Casual', 'Mellow', 'Poised', 'Amusing', 'Groundbreaking', 'Spiritual', 'Happy', 'Conservative',
       'Self-Conscious', 'Placid', 'Self-Disciplined', 'Ethical', 'Logical', 'Tolerant', 'Real', 'Robust',
       'Enterprising', 'Succinct', 'Adventuresome', 'Academic', 'Exuberant', 'Practical', 'Tolerable',
       'Appreciative', 'Fun', 'Passive', 'Pro-Active', 'Magical', 'Messy', 'Pitiful', 'Instinctive', 'Cheerful',
       'Confident', 'Hyperactive', 'Dazzling', 'Mighty', 'Respectful', 'Generous', 'Mild', 'Frank', 'Stimulating',
       'Funny', 'Plausible', 'Exclusive', 'Willing', 'Unusual', 'Righteous', 'Modest', 'Fascinating', 'Hypochondriac',
       'Ambitious', 'Sincere', 'Plucky', 'Smiling', 'Directed', 'Attractive', 'Imaginative', 'Integrity', 'Alluring',
       'Patient', 'Serious', 'Debonair', 'Spunky', 'Proper', 'Beautiful', 'Jovial', 'Lovely', 'Rude', 'Discriminating',
       'Merry', 'Personable', 'Tantalizing', 'Pioneering', 'Thoughtful', 'Successful', 'Studious', 'Excellent',
       'Careful', 'Lovable', 'Outgoing', 'Nervous', 'Moderate', 'Upbeat', 'Prudent', 'Carefree', 'Courteous',
       'Intuitive', 'Clever', 'Eclectic', 'Crazy', 'Unbiased', 'Complex', 'Affectionate', 'Original', 'Surprising',
       'Amused', 'Ugly', 'Poor', 'Efficient', 'Ingenious', 'Cool', 'Arrogant', 'Noisy', 'Fanatic', 'Unique', 'Shrewd',
       'Self-Sacrificing', 'Principled', 'Violent', 'Compassionate', 'Lively', 'Consistent',
       'Straightforward', 'Brave', 'Determined', 'Direct', 'Revered', 'Forceful', 'Flexible', 'Romantic', 'Intense',
       'Fun-Loving', 'Enthusiastic', 'Comfortable', 'Capable', 'Accurate', 'Careless', 'Seemly', 'Harmonious', 'Naïve',
       'Adorable', 'Responsible', 'Adept', 'Earnest', 'Exciting', 'Decorous', 'Rational', 'Sympathetic', 'Materialistic',
       'Considerate', 'Talented', 'Handsome', 'Firm', 'Responsive', 'Gracious', 'Impartial', 'Impromptu', 'Thrilling',
       'Boundless', 'Easygoing', 'Noble', 'Amazing', 'Adventurous', 'Thorough', 'Attentive', 'Unassuming', 'Agreeable',
       'Resourceful', 'Mature', 'Accepting', 'Bold', 'Dainty', 'Athletic', 'Fearless', 'Sensible', 'Punctual',
       'Professional', 'Encouraging', 'Leadership', 'Diplomatic', 'Fighter', 'Multi-Talented', 'Strong', 'Dominant',
       'Patriotic', 'Clumsy', 'Amiable', 'Hilarious', 'Tough', 'Decent', 'Kind-Hearted', 'Splendid', 'Learned',
       'Demented', 'Religious', 'Meticulous', 'Dynamic', 'Dashing', 'Fair-Minded', 'Amicable', 'Hard Working',
       'Hard-Working', 'High-Flier', 'Inscrutable', 'Communicative', 'Resolute', 'Deranged', 'Sensitive', 'Interesting',
       'Aware', 'Keen', 'Painstaking', 'Feminine', 'Relaxed', 'Selective', 'Problem-Solver', 'Spirited', 'Dedicated',
       'Steady', 'Unprecedented', 'Coherent', 'Light', 'Optimistic', 'Fancy', 'Melancholy', 'Skillful', 'Bossy',
       'Reverent', 'Rhetorical', 'Devoted', 'Self-Sufficient', 'Perfectionist', 'Alert', 'Wholesome', 'Intelligent',
       'Clean', 'Knowledgeable', 'Vigorous', 'Balanced', 'Philosophical', 'Methodical', 'Deliberate', 'Protective',
       'Peaceful', 'Good-Natured', 'Open-Minded', 'Independent', 'Articulate', 'Hermetic', 'Sociable', 'Kind',
       'Thrifty', 'Courageous', 'Inquisitive', 'Honorable',  'Adaptable', 'Emotional', 'Precise', 'Immature',
       'Discreet', 'Excited', 'Timid', 'Gregarious', 'Eager', 'Awkward', 'Supportive', 'Sharp', 'Mean', 'Nice',
       'Loveable', 'Cooperative', 'Stable', 'Self-Directed', 'Verbal', 'Giving', 'Steadfast', 'Faithful',
       'Sophisticated', 'Spontaneous', 'Gorgeous', 'Joyful', 'Empathetic', 'Strategic', 'Retiring', 'Fashionable',
       'Worthy', 'Industrious', 'Productive', 'Idealistic', 'Cultured', 'Friendly', 'Natural', 'Likeable',
       'Awesome', 'Trustworthy', 'Sedate', 'Relieved', 'Reliable', 'Prim', 'Boastful', 'Self-Assured', 'Credible',
       'Shy', 'Witty', 'Humorous', 'Dreamer', 'Expert', 'Manipulative', 'Tricky', 'Understanding', 'Tireless',
       'Resilient' , 'Questioning', 'Endurable', 'Trusting', 'Lucky', 'Likable', 'Mannerly', 'Detailed',
       'Influential', 'Insightful', 'Composed', 'Neat', 'Good', 'Self-Confident', 'Reserved', 'Persistent', 'Tactful',
       'Demanding', 'Loyal', 'Organized', 'Bright', 'Frustrated', 'Embarrassed', 'Smart', 'Elated', 'Calm', 'Observant',
       'Stubborn', 'Tender', 'Haggard', 'Assertive', 'Popular', 'Grouchy', 'Unselfish', 'Opinionated', 'Peaceable',
       'Immaculate', 'Honest', 'Daring', 'Devout', 'Memorable', 'Active', 'Decisive', 'Glorious', 'Judgmental',
       'Self-Starter', 'Sharp-Witted', 'Quick', 'Broad-Minded', 'Modern', 'Fair Minded', 'Busy', 'Leisurely',
       'Respectable', 'Fervent', 'Dignified', 'Tense', 'Silly', 'Energetic', 'Charming', 'Obedient', 'Venerable',
       'Warm', 'Healthy', 'Powerful', 'Nurturing', 'Perky', 'Level', 'Reflective']
adj_pos = ["Positive", " Rich " , 'Pleasant']