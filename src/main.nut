require("version.nut");


class TBMain extends GSController 
{
	constructor()
	{
	}

	function Init();
	function HandleEvents();
}

function TBMain::Start()
{
	this.Init();

	GSController.Sleep(1);

	while (true) {
		this.HandleEvents();

		GSController.Sleep(1);
	}
}

function TBMain::Init()
{
}

function TBMain::HandleEvents()
{
}

function TBMain::Save()
{
	return {};
}

function TBMain::Load(version, tbl)
{
}
