from Trick import FlatTrick, GrindTrick, SlideTrick, ManualTrick, CombinationTrick
from Obstacles import Box, Manualpad, Rail, Kicker, Flatground


tricks = {
	"kickflip" : FlatTrick("Kickflip", 0, -1, 0),
	"ollie" : FlatTrick("Ollie", 0, 0, 0),
	"heelflip" : FlatTrick("Heelflip", 0, 1, 0),
	"backside180" : FlatTrick("Backside 180", 1, 0, 1),
	"frontside180" : FlatTrick("Frontside 180", -1, 0, -1),
	"backsidebigspin" : FlatTrick("Backside Bigspin", 2, 0, 1),
	"frontsidebigspin" : FlatTrick("Frontside Bigspin", -2, 0, 1),
	"grind5050" : GrindTrick("50-50"),
	"treflip" : FlatTrick("360 Flip", 2, -1, 0),
	"crookedgrind" : GrindTrick("Crooked Grind"),
	"50-50" : GrindTrick("50-50"),
	"5-0" : GrindTrick("5-0"),
	"nosegrind" : GrindTrick("Nose Grind"),
	"feeblegrind" : GrindTrick("Feeble Grind"),
	"smithgrind" : GrindTrick("Smith Grind"),
	"noseslide" : SlideTrick("Nose Slide"),
	"tailslide" : SlideTrick("Tail Slide"),
	"boardslide" : SlideTrick("Board Slide"),
	"darkslide" : SlideTrick("Dark Slide"),
	"nosemanual" : ManualTrick("Nose Manual"),
	"manual" : ManualTrick("Regular Manual")
}

obstacles = {
	"box" : Box(30, 70, 200),
	"flatground" : Flatground(),
	"rail" : Rail(40, 250),
	"kicker" : Kicker(40, 70),
	"manualpad" : Manualpad(30, 60, 250),
	"stairs" : Flatground()
}

combinationTricks = {



}

lines = {

}