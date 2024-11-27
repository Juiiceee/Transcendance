import GameLocal from "../../../../local/GameLocal.js";
import Game from "../../../Game.js";

export class BaseMap {
	constructor(game) {
		if (!game || (!(game instanceof Game) && !(game instanceof GameLocal))) {
			throw new Error('Invalid game instance');
		}
		this.game = game;
	}

	update() {
	}
}