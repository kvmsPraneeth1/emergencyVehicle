//
// Copyright (C) 2017 Christoph Sommer <sommer@ccs-labs.org>
//
// Documentation for these modules is at http://veins.car2x.org/
//
// SPDX-License-Identifier: GPL-2.0-or-later
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//

package projecta.simulations.sumoSimulation;


import org.car2x.veins.nodes.RSU;
import org.car2x.veins.nodes.Scenario2;
import org.car2x.veins.nodes.TrafficLight;

network RSUExampleScenario extends Scenario2
{
    submodules:
        rsu[1]: RSU {
            @display("p=542.0119,8.284024;i=veins/sign/yellowdiamond;is=vs");
        }

        tls[0]: TrafficLight;
        rsu2[1]: RSU {
            @display("p=541.42017,9.467457;i=veins/sign/yellowdiamond;is=vs");
        }

        rsu3[1]: RSU {
            @display("p=540.8284,8.875741;i=veins/sign/yellowdiamond;is=vs");
        }

        rsu4[1]: RSU {
            @display("p=540.8284,9.467457;i=veins/sign/yellowdiamond;is=vs");
        }

        rsu5[1]: RSU {
            @display("p=537.27814,7.6923084;i=veins/sign/yellowdiamond;is=vs");
        }

        rsu6[1]: RSU {
            @display("p=537.27814,10.650888;i=veins/sign/yellowdiamond;is=vs");
        }

        rsu8[1]: RSU {
            @display("p=538.4616,10.059173;i=veins/sign/yellowdiamond;is=vs");
        }

        rsu9[1]: RSU {
            @display("p=535.503,13.609468;i=veins/sign/yellowdiamond;is=vs");
        }

}
