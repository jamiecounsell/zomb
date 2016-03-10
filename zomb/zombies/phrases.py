

ZOMBIE_TYPES = [
    "tough",
    "fast",
    "angry",
    "swollen",
    "really fast",
    "armless",
    "legless",
    "head-only",
    "nice",
    "handsome",
    "rotten",
    "harmless",
    "quiet",
    "bloated",
    "yellow",
    "smelly",
    "sexy",

]

ZOMBIE_HOMETOWNS = [
    "Accident, a town in Maryland, United States. It was really created by an accident!",
    "Alert, a weather station settlement in Nunavut, Canada, that, by its cold temperatures, doesn't look very alert",
    "Apocalypse Peaks, a group of peaks in Antarctica, which would make a very anticlimactic apocalypse",
    "Arcade, a town in Veneto, Italy",
    "Athol, a town in Massachusetts, USA",
    "Bat, a city on Israel's Mediterranean Coast",
    "Bell End, a village in Worcestershire, England. Bell end is British slang for the head of the penis",
    "Beer, a village in Devon, England",
    "Berry Head, a settlement in Newfoundland and Labrador, Canada and a point near Brixham, United Kingdom",
    "Big Beaver, a town in Saskatchewan, Canada and another in Beaver County, Pennsylvania, both sharing some big beavers",
    "Bird-in-Hand, a town in Pennsylvania, USA",
    "Bitter End, a town in Tennessee, USA",
    "Bong, a county in Liberia, named for its Mount Bong",
    "Brown, a hill in Cornwall that gave its name to the Brown Willy effect",
    "Catbrain, a village in South Gloucestershire, England. Everyone in there has a cat brain!",
    "Christmas Pie, a hamlet in Surrey, England",
    "Circle, a small town in Alaska originally believed to lie on the Arctic Circle, though it is actually about 50 miles (80 km) away",
    "Clitheroe, a town in Lancashire, England",
    "Coffin Top, a mountain on South Georgia. This is where all the dead Georgians are put",
    "Desire, a town in Pennsylvania, USA",
    "Devil Town, a ghost town in Ohio, USA",
    "Devil's, a big hill in County Tipperary, Ireland",
    "Devilsmother, a big hill in County Galway, Ireland. It could also mean smothering the devil",
    "Dinosaur, a Statutory Town located in Moffat County, Colorado, United States",
    "DISH, a small town in Texas that changed its name to receive free digital video recorders and satellite television for ten years",
    "Dinga, a city in Punjab province of Pakistan",
    "Dog, a Hamlet in Devon, United Kingdom near Broadclyst",
    "Dolphin's Barn, a barn for land dolphins",
    "Earth, a town in Texas, United States of America",
    "Executive Committee Range, a mountain range in Antarctica",
    "Fair Play, a town in New Jersey, USA",
    "Feltwell, a village in Norfolk, England",
    "Fifty-Six, a city in northern Arkansas",
    "Football Mountain, a mountain in Antarctica. Eskimos play football here!",
    "Frenchbeer, a small Hamlet in Devon, United Kingdom",
    "George, a town in central Washington. The streets are named after varieties of cherries",
    "Good, a town in New Jersey, USA",
    "Great, a New York City neighborhood. I've heard some parts of New York can be violent..",
    "Happy, a village in Newfoundland and Labrador, Canada",
    "House, a village in New Mexico, in which yes, there is at least one house",
    "Hooker  A town in Oklahoma,, a that is probably too small for a prostitution business",
    "Hazard, a city in and the county seat of Perry County, Kentucky",
    "Hop Bottom, a borough in Pennsylvania, USA",
    "Hospital, a village without a hospital in County Limerick, Ireland",
    "Humptulips, a small town in Washington state, USA",
    "Humpty Doo  I wonder if Humpty fell here, a town 40 kilometres (25 mi) from Darwin, Northern Territory, australia",
    "Jersey Shore, a town located over 100 miles (160 km) from New Jersey",
    "Jim Thorpe, a borough in Pennsylvania bearing the name of Jim Thorpe",
    "Joe Batt's Arm, a town in Newfoundland and Labrador, Canada. Who's Joe Batt?",
    "Kfar Pines, a town in Northern Israel. The second word is pronounced like 'penis'",
    "Kilbride, a neighbourhood of St. John's, Newfoundland and Labrador, Canada where marriages end horribly",
    "Killinaboy, a village, townland and civil parish in County Clare, Ireland",
    "Lemu, a county in Finland. Translates to Stink",
    "Littlejoy Road, a road in Newton Abbot, England. There's little joy there!",
    "Lizard, a village in Cornwall",
    "Lost, a genuine Scottish hamlet's name",
    "Lucky Boy, a ghost town in Nevada, USA",
    "Mianus, a neighborhood in Greenwich, Connecticut",
    "Mistake Peak, a mountain peak in Antarctica. Man, it was really an accident!",
    "Moneymore, a place where you'll earn more money",
    "Mooball[3], a town in New South Wales, australia",
    "Moose Jaw, a city in Saskatchewan, Canada",
    "More Tomorrow, a village in Cayo District, Belize",
    "Mount, a mountain in Antarctica",
    "Mount, a mountain peak in Antarctica. Kills people!",
    "Mount Terror, a great place for a family picnic",
    "Mount Toogood, a mountain in Antarctica",
    "Muff, a village in County Donegal, Ireland",
    "Nobber, a village in County Meath, Ireland",
    "No Man's Land, a Small Hamlet in Cornwall, United Kingdom",
    "Nork, a town in Surrey, England, on the border with London. Also a suburb of Yerevan, armenia",
    "Normal, a town in Illinois, USA. Home of Illinois's first public university, Illinois State University. All in all, pretty normal",
    "North Piddle, a parish in Worcestershire, England",
    "Odd Down, a suburb of the English city of Bath, Somerset",
    "Ofakim, a city in southern Israel that seems to have been named by someone who was pretty exasperated with some dude",
    "Ogre, a city in Central Latvia",
    "Pill, a village in North Somerset, England, which does have a chemist",
    "Poundsgate, a village in Devon, England",
    "Pratt's Bottom, a village in the London Borough of Bromley, originally Spratts Bottom",
    "Pray, a very religious Italian town",
    "Puddletown  A village in Dorset, United Kingdom, a town of puddles",
    "Punkeydoodles Corners, a hamlet in Ontario known for its name and frequent sign theft",
    "Red Deer, a city in Alberta, Canada",
    "Rock, a village in Cornwall",
    "Scratchy, a clifftop valley near Durdle Door, Weymouth in Dorset, England",
    "Shop, a village in Cornwall, England",
    "Shortlands, a not very big borough in London, England",
    "Six Mile, a village in Cambridgeshire, England",
    "Slave Lake, a town in Alberta, Canada",
    "Sofia University Mountains, a mountain range in Antarctica",
    "Superior, a town in West Virginia, USA",
    "Supporting Party Mountain, a mountain in Antarctica",
    "Te, a town in New Zealand, known for kiwifruit packing and a wood processing plant called Pukepine",
    "Three, a village in Powys, Wales. More commonly known by its Welsh name Aberllynfi",
    "Truth or Consequences, a town in New Mexico that renamed itself simply so it could host the show that bore its name",
    "Unalaska, a town in Alaska whose name makes it sound like it's not happy with its situation",
    "Useless Loop, a very small town in Western Australia",
    "Wallyford, a town in East Lothian, Scotland",
    "What Cheer, a small coal town in Keokuk County, Iowa",
    "Wideopen, a village in Northumbria, near Newcastle upon Tyne",
]

ZOMBIE_HOBBIES = [
    "Telescope Making",
    "Spelunking",
    "Rock Collecting",
    "Knifemaking",
    "Home Brewing",
    "Woodworking",
    "Cooking",
    "Film Making",
    "Doll Making",
    "Sewing",
    "Book Making",
    "Glass Blowing",
    "Wargame terrain making",
    "Scrapbooking",
    "Candlemaking",
    "Painting and Drawing",
    "Jewelry Making",
    "Glass Blowing",
    "Weaving",
    "Soapmaking",
    "Quilling",
    "Paper Making",
    "Wood Carving",
    "Engraving",
    "Beadwork and beading",
    "Wire Jewelry making",
    "Tole Painting",
    "GunSmithing",
    "Hiking",
    "Rock Climbing",
    "Nature Walking",
    "Mountain Climbing",
    "Bird Watching",
    "Four Wheeling",
    "Rafting/Canoeing",
    "Butterfly collecting and watching",
    "Backpacking",
    "Bouldering",
    "Gardening",
    "Organic Gardening",
    "Fishing",
    "Geocaching",
    "Ghosthunting",
    "Horse Riding",
    "Paintballing",
    "Snorkeling",
    "Scuba Diving",
    "Skiing",
    "Surfing",
    "Skateboarding",
    "Spelunking",
    "Skydiving",
    "Fencing",
    "Golfing",
    "Hang Gliding",
    "Hot Air Ballooning",
    "Sailing",
    "Ballet Dancing",
    "Belly Dancing",
    "Bungee Jumping",
    "Fly Fishing",
    "Gold Panning",
    "Astronomy",
    "Microscopy",
    "Model Rocketry",
    "Model airplanes",
    "Making Dioramas",
    "Making Telescopes",
    "Making Musical Instruments",
    "Blacksmithing"
]

ZOMBIE_NAMES = [
    "Abby",
    "Ady",
    "Amity",
    "Anne",
    "Anton",
    "Ariadne",
    "Bob",
    "Brandy",
    "Bridget",
    "Brody",
    "Cecil",
    "Charlie",
    "Charlotte",
    "Cindy",
    "Cole",
    "Colton",
    "Conner",
    "Dalila",
    "Deidra",
    "Drake",
    "Dylan",
    "Emily",
    "Eric",
    "Fausto",
    "Feng",
    "Francisco",
    "Grant",
    "Hawkins",
    "Hendrik",
    "Henry",
    "Herbert",
    "Hunter",
    "Issac",
    "Jack",
    "Janey",
    "Jasmine",
    "Jericho",
    "Johanna",
    "Karen",
    "Kari",
    "Lacy",
    "Lawson",
    "Liam",
    "Lillian",
    "Lucas",
    "Lucretia",
    "MacLaren",
    "Maggie",
    "Malissa",
    "Margaret",
    "Michael",
    "Morgan",
    "Mort",
    "Neil",
    "Nicholas",
    "O\'Shea",
    "Petra",
    "Reed",
    "Ross",
    "Roz",
    "Sandy",
    "Selina",
    "Sherie",
    "Subodh",
    "Thad",
    "Ursula",
    "York",
]