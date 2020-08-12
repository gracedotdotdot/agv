
"use strict";

let GPS = require('./GPS.js');
let Goal = require('./Goal.js');
let KeyPoint = require('./KeyPoint.js');
let OdomInfo = require('./OdomInfo.js');
let Path = require('./Path.js');
let GlobalDescriptor = require('./GlobalDescriptor.js');
let UserData = require('./UserData.js');
let MapData = require('./MapData.js');
let NodeData = require('./NodeData.js');
let MapGraph = require('./MapGraph.js');
let Point3f = require('./Point3f.js');
let Point2f = require('./Point2f.js');
let Info = require('./Info.js');
let Link = require('./Link.js');
let RGBDImage = require('./RGBDImage.js');
let ScanDescriptor = require('./ScanDescriptor.js');

module.exports = {
  GPS: GPS,
  Goal: Goal,
  KeyPoint: KeyPoint,
  OdomInfo: OdomInfo,
  Path: Path,
  GlobalDescriptor: GlobalDescriptor,
  UserData: UserData,
  MapData: MapData,
  NodeData: NodeData,
  MapGraph: MapGraph,
  Point3f: Point3f,
  Point2f: Point2f,
  Info: Info,
  Link: Link,
  RGBDImage: RGBDImage,
  ScanDescriptor: ScanDescriptor,
};
