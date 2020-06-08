﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using TomorrowDiesToday.Models.Enums;

namespace TomorrowDiesToday.Models
{
    public class TileStats
    {
        public Stat Combat { get; set; }

        public Stat Cunning { get; set; }

        public Stat Diplomacy { get; set; }

        public Stat Stealth { get; set; }

        public TileStats()
        {
            // Initialize Stats List
            Combat = new Stat(StatType.Combat);
            Cunning = new Stat(StatType.Stealth);
            Diplomacy = new Stat(StatType.Cunning);
            Stealth = new Stat(StatType.Diplomacy);
        }

        public TileStats(int combat, int stealth, int cunning, int diplomacy)
        {
            // Initialize Stats List
            Combat = new Stat(StatType.Combat, combat);
            Cunning = new Stat(StatType.Cunning, cunning);
            Diplomacy = new Stat(StatType.Diplomacy, diplomacy);
            Stealth = new Stat(StatType.Stealth, stealth);
        }

        public TileStats IncreaseAll(int modifier)
        {
            return new TileStats(Combat.Value + modifier, Stealth.Value + modifier, Cunning.Value + modifier, Diplomacy.Value + modifier);
        }

        public TileStats MultiplyAll(int multiplier)
        {
            return new TileStats(Combat.Value * multiplier, Stealth.Value * multiplier, Cunning.Value * multiplier, Diplomacy.Value * multiplier);
        }
    }
}