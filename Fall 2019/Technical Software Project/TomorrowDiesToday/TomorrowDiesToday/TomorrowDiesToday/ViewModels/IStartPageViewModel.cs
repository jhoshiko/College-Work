﻿using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Text;
using System.Windows.Input;
using TomorrowDiesToday.Models;

namespace TomorrowDiesToday.ViewModels
{
    public interface IStartPageViewModel
    {
        ICommand CreateGameCommand { get; }
        ICommand JoinGameCommand { get; }
    }   
}       
        