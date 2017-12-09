BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `music` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`file_id`	TEXT NOT NULL UNIQUE,
	`right_answer`	TEXT NOT NULL,
	`wrong_answer`	TEXT NOT NULL
);
INSERT INTO `music` (ID,file_id,right_answer,wrong_answer) VALUES (1,'AwADAgADMgEAAiDwYEl3JTFYyeki5AI','Homer','Andrew,Vova,Your mum');
COMMIT;
