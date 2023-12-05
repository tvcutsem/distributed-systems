// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.7;

contract NameRegistry {
   
   mapping (string => address) public registry;

   constructor() {}

   function claimName(string calldata name) public payable {
       require(msg.value >= 1 ether);
       if (registry[name] == address(0)) {
           registry[name] = msg.sender;
       }
   }

   function ownerOf(string calldata name) public view returns (address) {
       return registry[name];
   }
}